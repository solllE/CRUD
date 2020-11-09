from django.shortcuts import render, redirect
from .models import Post, Comment

# POST는 내가 만든 모델 객체!!!!! 원래 있던거 아님
# 메인 페이지
def main(request):
    return render(request, 'main.html')

# 작성 페이지
def new(request):
    return render(request, 'new.html')

# 작성 기능 함수
# 데이터베이스에 내용을 저장하는 행위는 데이터를 가져오는 역할을 하는 GET 방식보다는 POST 방식과 더 적합
# 또한, POST 방식으로 데이터를 실어서 요청을 보낼 경우, 주소창에 데이터가 표시되지 않으므로 보안적인 측면에도 더 나음
def create(requset):
    
    # POST 방식으로 웹에서 제목과 내용을 가져와 각 변수에 저장
    getTitle = requset.POST.get('title')
    getContent = requset.POST.get('content')

    # DB의 title 컬럼과 content 컬럼에 웹에서 가져온 내용을 저장 (Post 클래스를 이용하여 DB에 조작을 가함)
    post = Post(title=getTitle, content=getContent)
    post.save()
    
    # post 방식은 html을 반환하지 않기 때문에 render(html을 반환하는)가 아닌 redirect(바로 특정 페이지로 리다이렉트)를 사용
    return redirect('board:detail', post.pk)

# 리스트 보여주는 페이지
def index(request):
    posts = Post.objects.all()  # 모델 Post내 DB에 저장된 모든 값을 불러와(objects.all()) posts에 저장
    # DB에서 가져온 값들을 posts에 저장하고 index.html의 posts에 전달해서 불러온다
    return render(request, 'index.html', {'posts': posts})


# 세부 내용 보여주는 페이지
def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})

# 삭제 기능
# 1. detail.html 에서 삭제 버튼을 누르면 /board/{{post.pk}}/delete 로 url 요청
# 2. 요청된 url과 매핑된 delete 함수 실행
# 3. 함수 내용대로 전달받은 프라이머리키의 글을 삭제하고 /board/index로 리다이렉트
# 4. 요청된 url과 매핑된 index 함수 실행하여 게시글 목록을 보여줌
def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()

    return redirect('board:index')

# 수정 기능
# 1. detail.html 에서 삭제 버튼을 누르면 /board/{{post.pk}}/edit 로 url 요청
# 2. 요청된 url과 매핑된 edit 함수 실행하여 수정 화면 나오게 함
# 3. 수정하여 submit 버튼을 누르면 /board/{{post.pk}}/update/ 로 url 요청
# 4. 요청된 url과 매핑된 update 함수 실행하여 수정 기능 수행하고 /board/{post_id}/로 리다이렉트
# 5. 리다이렉트 된 url 과 매핑된 detail 함수 실행하여 수정 내용 보여줌

# 수정 내용 작성 페이지
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(request, 'edit.html', {'post':post})

# 수정 기능 함수
def update(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()

    return redirect('board:detail', post.pk)

# Comment 내용

# 댓글 작성
def comments_create(request, post_id):
    post = Post.objects.get(pk=post_id) # 댓글 달 게시물에 대한 정보 가져옴
    content = request.POST.get('content')   # 폼 태그에서 넘어온 댓글 내용 가져옴

    # 댓글 생성 및 저장
    comment = Comment(post=post, content=content)
    comment.save()

    # 댓글 생성 후 디테일 페이지로 리다이렉트
    return redirect('board:detail', post.pk)

# 댓글 삭제 기능
def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()

    return redirect('board:detail', post_id)
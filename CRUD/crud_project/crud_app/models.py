from django.db import models

# 게시글 관련 스키마 정의
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

# 댓글 관련 스키마 정의
class Comment(models.Model):

    # Foreingnkey(외래키가 연결되는 테이블 입력(여기서는 Post),
    #             외래키가 보는 값이 삭제시 처리 옵션)
    # -> 외래키 설정하는 함수

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
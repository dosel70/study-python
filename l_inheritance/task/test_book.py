# 상속 예제
# 게시글 - 댓글
# 게시글 번호와 댓글 번호는 자동 증가
# 게시글 class에 게시들 정보 출력 메소드를 만들고
# 댓글 class에서 정보 출력 메소드를 상속받고 댓글 정보 추가하여 출력
# 게시글: 게시글 번호, 작성자, 제목, 내용
# 댓글: 댓글 번호, 게시글 번호, 작성자, 댓글 내용
class Post:
    post_count = 0 # 게시글 번호

    def __init__(self,writer,title,content) :
        Post.post_count += 1 # 게시글 번호는 1부터 시작으로 설정함
        self.post_number = Post.post_count
        self.writer = writer
        self.title = title
        self.content = content

    def post_info(self):
        print(f"게시글 번호: {self.post_number}")
        print(f"작성자 : {self.writer}")
        print(f"제목 : {self.title}")
        print(f"내용 : {self.content}")
        print("\n")

class Comment(Post):
    comment_count = 0

    def __init__(self,post,writer,comment_content):
        Comment.comment_count += 1
        super().__init__(writer=writer, title=f"{post.title}", content=comment_content)
        self.comment_number = Comment.comment_count
        self.post_number = post.post_number
        self.writer = writer
        self.comment_content = comment_content

    def comment_info(self):
        print(f"댓글 번호 : {self.comment_number}")
        print(f"게시글 번호 : {self.post_number}")
        print(f"작성자 정보 : {self.writer}")
        print(f"댓글 정보 : {self.comment_content}")
        print("\n")

post1 = Post(writer="홍길동", title="1번 제목", content="텍스트 내용")


post1.post_info()


comment1 = Comment(post=post1, writer="홍길동", comment_content="댓글 내용")


comment1.comment_info()


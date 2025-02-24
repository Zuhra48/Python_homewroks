class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(f"Title: {post.title}, Author: {post.author}")

    def display_posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"Title: {post.title}, Content: {post.content}")


def main():
    blog = Blog()
    
    while True:
        print("\nOptions: 1. Add Post 2. List Posts 3. Posts by Author 4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added!")
        elif choice == "2":
            blog.list_posts()
        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_posts_by_author(author)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def delete_post(self, title):
    for post in self.posts:
        if post.title == title:
            self.posts.remove(post)
            print(f"Post titled '{title}' deleted.")
            return
    print("Post not found.")















class Task:
    def _init_(self,title,description,due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = 'incomplete'


    def mark_complete(self):
        self.status = 'complete'

    def _str_(self):
        return f'Title:{self.title}, Description: {self.description},Due_date:{self.due_date}' 


    class ToDoList:
        def _init_(self):
            self.tasks = []

        def add_tasks(self, title, description, due_date):
            task = Task(title, description, due_date)
            self.tasks.append(task)


        def mark_task_complete(self,task_title):
            for task in self.tasks:
                if task.title == task_title and task.status =='incomplete':
                    task.mark.complete()
                    break      
                   
        def main():
            todo_list = ToDoList()

            while True:
                print("\nTo_Do List Menu:")
                print("1.Vazifa qo'shish")
                print("2. Vazifani bajarilgan deb belgilash")
                print("3. Barcha vazifalarni ko'rsatish")
                print("4. Faqat bajarilmagan vazifalarni ko'rsatish")
                print("5. Chiqish")

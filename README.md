# Apile

![stack by Zach Bogart from the Noun Project](noun-stack.png)

For this week's project, you will build as a group a Django application that users use to collect links, and vote and comment on these links. This is like [Hacker News](https://news.ycombinator.com/), [Reddit](https://www.reddit.com/), or [Lobsters](https://lobste.rs/).

## Specifications

### Models

- The focus of the application is the concept of "posts". Posts are what users add, vote on, and comment on. Each post must have an author (the user who created it) and a title. Each post can have a link and a description. If a post doesn't have a link, then it exists just for commenting -- it's usually a question.
- Posts belong to a user, the author. Posts have many comments and votes.
- Votes belong to a user, the voter, and a post.
- Comments belong to a user, the author, and a post.
- Users have many posts, comments, and votes.

### Interface

- The application's styling should look intentional, but does not have to be elaborate. You can use any CSS framework you like, or create your own CSS.
- The main page of the application shows a paginated list of posts. This list of posts is ordered by the number of votes (most votes at the top, descending) and the datetime the post is added (again, descending). The user should be able to choose to sort by number of votes first (with datetime as a secondary sort for ties) or by datetime first.
  - Note the word _paginated_. These links should be paginated, with each page showing 20 links. Consider using a third-party library for pagination or roll your own with GET parameters.
- Clicking on thumbs-up (or some other icon you choose) on a post should add a positive vote to that post. The user should come back to the same page they are currently on after clicking. A user can only vote once on a post.
  - What's the best way to make this work without JavaScript? Each link can have an id, and the user can be redirected back to the page they're on with an anchor for that id after upvoting.
- Clicking on a post's title should take the user to the post's link, if it has one. If not, it takes the user to the post's detail page.
- Each post displayed should also show the number of comments it currently has. Clicking that number of comments should take the user to the post's detail page.
- On the post's detail page, the post title and description should be shown, along with all the post's comments, ordered by datetime created ascending (first comment to most recent). Each comment should show the user who created it.
- Posts can be viewed by anyone, but only a signed-in user can comment or vote.
- The [Django messages framework](https://docs.djangoproject.com/en/2.1/ref/contrib/messages/) should be used for informing the user

When a user is signed in:

- They can create posts.
- They can vote on posts.
- They can create comments on posts.
- They can delete posts they created.
- They can delete comments they created.

Optional ideas for enhancing this application:

- Add a profile page for a user that displayed all the posts a user has created and all comments they have made.
- Allow users to edit their comments.
- Add search functionality.

### Development and deployment

- This application must be deployed to Heroku.
- This application must have a management command to create some initial data. There should be at least 30 posts, each with votes and comments, in the initial data. There should be at least 10 users used to make these. The posts and comments don't have to make sense. Consider using [Faker](https://faker.readthedocs.io/en/master/) or [Mimesis](https://mimesis.readthedocs.io/) to create your initial data.

### Other notes

The above are requirements necessary for this assignment to be complete. This is your first group project, so completion is evaluated, unlike previous assignments. With that said, please use your creativity to add new ideas to this. Do you want to try to add hashtags, with pages that show all posts with a particular hashtag? Go for it! Do you have a feature you've thought of you've never seen elsewhere? That is great and you should try to implement it! Learning happens when we stretch ourselves in this way.

## Resources

- [Font Awesome Icons](https://fontawesome.com/)
- [Faker](https://faker.readthedocs.io/en/master/) and [Mimesis](https://mimesis.readthedocs.io/)
- [dj-pagination](https://dj-pagination.readthedocs.io/en/latest/)
- [Django-Gravatar](https://github.com/twaddington/django-gravatar/) -- add user avatars!
- [django-find](https://github.com/knipknap/django-find) -- add search

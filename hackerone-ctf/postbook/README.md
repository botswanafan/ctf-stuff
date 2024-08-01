# Postbook
## Flag 1:
  - Upon viewing the website, and seeing how it loads the blogs, I found that it identifies them by an id at the end of the url, similar to: 'index.php?page=view.php&id=2', where 2 is the id.
  - Viewing the page with the id 2, I found the first flag.

  Alternative method to get the flag:
  - Since the profile page is identified via letters, I found that you can change, 'index.php?page=profile.php&id=d' to 'index.php?page=profile.php&id=a' to get more pages. You can also change the last a to a b, c, or d to view some more information
## Flag 2:
  - I found that there was a hidden element on the webpage, that was similar to `<input type="hidden" name="user_id" value="3">`. I then just removed the hidden portion and modified the value to be 5, which seemed to get the flag.
## Flag 3:
- There is a user whose username is `user` and password is `password`. I logged in with these credentials and found the flag in the profile page.
## Flag 4:
- You can edit any user's post by changing the `id` parameter in the URL. I changed the `id` parameter to 1 and edited the post to get the flag.

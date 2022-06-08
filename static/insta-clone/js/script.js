$(document).ready(function () {
  $(".comment-form").submit(addComment);
  $(".post-image").dblclick(like);
  $(".dislike").click(dislike);
});
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie("csrftoken");

const addComment = (e) => {
  e.preventDefault();
  const comment = e.target[1];
  const postId = e.currentTarget.id.slice(11);
  if (comment.value.length < 2) {
    comment.classList.add("is-invalid");
  } else {
    comment.classList.remove("is-invalid");
    return createComment(postId, comment, comment.value);
  }
};

const createComment = (postId, comment_form, comment) => {
  $.ajax("/posts/comments/create/", {
    type: "POST",
    headers: {
      "X-CSRFToken": csrftoken,
      mode: "same-origin", // Do not send CSRF token to another domain.
    },
    data: { postId: postId, comment: comment },
    success: function (data) {
      comment_form.value = "";
      reloadWindow();
    },
    error: function (error) {},
  });
};

const like = (e) => {
  const likeBtn = e.target.previousElementSibling;
  const postId = e.target.id.slice(4);
  $(likeBtn).show();
  setTimeout(() => {
    $(likeBtn).hide();
  }, 1200);
	addToLikes(postId);
};

const dislike = (e) => {
  const postId = e.target.id.slice(7);
  return removeToLikes(postId);
};

const addToLikes = (postId) => {
  $.ajax({
    type: "POST",
    url: "/posts/likes/like/",
    headers: {
      "X-CSRFToken": csrftoken,
      mode: "same-origin",
    },
    data: { id: postId },
    success: function (data) {
      setTimeout(() => {
				reloadWindow();
			}, 1000);	
    },
    error: function (jqXHR, textStatus, errorThrown) {},
  });
};

const removeToLikes = (postId) => {
  $.ajax({
    type: "POST",
    url: "/posts/likes/dislike/",
    headers: {
      "X-CSRFToken": csrftoken,
      mode: "same-origin",
    },
    data: { id: postId },
    success: function (data) {
      reloadWindow();
    },
    error: function (jqXHR, textStatus, errorThrown) {},
  });
};

const reloadWindow = () => {
  window.location.reload();
};


const toggleFollower = e => {
  const follower = e.target.id;
  const currentUserId = "";

}
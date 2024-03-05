const posts = [
  { title: 'Post One', body: 'this is post one' },
  { title: 'Post Two', body: 'this is post two' },
];

function getPost() {
  setTimeout(() => {
    let output = '';
    posts.forEach((post, index) => {
      output += `<li>${post.title}</li>`;
    });
    document.body.innerHTML = output;
  }, 1000);
}

function createPost(post) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      posts.push(post);

      const error = true;

      if (!error) {
        resolve();
      } else {
        reject('Error: Something went wrong ');
      }
    }, 2000);
  });
}

createPost({ title: 'Post Three', body: 'This is post three' }).then(getPost);

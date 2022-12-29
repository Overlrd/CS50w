// wait for the DOm content to load
document.addEventListener('DOMContentLoaded', function (){
// on headers click
document.querySelector('#all-posts').addEventListener('click', () => load_post('all'))
document.querySelector('#add-post').addEventListener('click', () => compose())

// by default load new post
compose()

function load_post(which){
        history.pushState({'posts':which}, '', ``);


        // hide other view

        document.querySelector('#all-posts-view').style.display = 'block';
        document.querySelector('#compose-view').style.display = 'none';
        //document.querySelector('#all-posts-view').innerHTML = `<h3>${which.charAt(0).toUpperCase() + which.slice(1)} Posts</h3>`;

        //fetch for the posts
        fetch(`/posts/${which}`)
        .then(response => response.json())
        .then(posts => {
            console.log(posts)
            for (const post of posts){
                post_id = post['id']
                post_user = post['user']
                post_content = post['body']
                post_timestamp = post['timestamp']
                post_num_like = post['likes']
    
    
                post_container = document.createElement('div');
                post_container.id = `post-container-${post_id}`
                post_container.className += "tweet_container"
    
                post_container.innerHTML = `
                <div class="image_container">
                <img  src="https://i.imgur.com/0PmI3ZD.png" alt="" srcset="">                    
                </div>


                <div class="tweet_body_container" >
                    <div class="tweet_header_container">
                        <span class="tweet_username" >${post_user}</span>  <span class="tweet_user_at" >SudoOverloord</span> <span class="tweet_date">${post_timestamp}</span>

                    </div>
                    <div class="tweet_body_text">
                        <p id="tweet_body_text">
                            ${post_content}
                        </p>
                    </div>
                    <div class="tweet_footer">
                        <div class="tweet_footer_item">
                            <span>
                                <i class="fa-regular fa-heart"></i>
                            </span>
                            <p>${post_num_like}</p>
                        </div>

                        <div class="tweet_footer_item">
                            <span>
                                <i class="fa-regular fa-heart"></i>
                            </span>
                            <p>15</p>
                        </div>

                        <div class="tweet_footer_item">
                            <span>
                                <i class="fa-regular fa-heart"></i>
                            </span>
                            <p>15</p>
                        </div>


                    </div>
                </div>

                `


                document.querySelector('#all-posts-view').appendChild(post_container)    
            }
        });
    
}


function compose(){
    document.querySelector('#all-posts-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
}


// function write post
document.querySelector('#compose-form').onsubmit = () => {
    const body = document.querySelector('#compose-body').value;
    // pass a post request to the backend
    fetch('/posts', {
    method: 'POST',
    body: JSON.stringify({
        body: body
    })
    })
    .then(response => response.json())
    .then(function () {
        alert('sent done')
    });
    }
    

})
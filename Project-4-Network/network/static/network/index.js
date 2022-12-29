// wait for the DOm content to load
document.addEventListener('DOMContentLoaded', function (){
// on headers click
document.querySelector('#all-posts').addEventListener('click', () => load_post('all'))
document.querySelector('#add-post').addEventListener('click', () => compose())

// overlay functions



function overlay_on() {
    document.getElementById("overlay").style.display = "block";
  }
  
function overlay_off() {
document.getElementById("overlay").style.display = "none";
}

document.querySelector('#close_span').addEventListener('click', function (){
    overlay_off()
})

function popify(view){
    overlay_on()
    element = document.querySelector(`${view}`).animate([
      // keyframes
      {opacity: '0'},
      {opacity : '1'}
    ],
    // timing options
    {
      duration:1000,
  
    })}

// by default load new post
load_post('all')

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
                if( parseInt(post_num_like) > 0 ){
                    liked = "liked";}
                else {
                    liked=''
                }
    
    
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
                                <i class="fa-solid fa-heart ${liked}"></i>
                            </span>
                            <p>${post_num_like}</p>
                        </div>

                    </div>
                </div>
                `
                document.querySelector('#all-posts-view').appendChild(post_container)    
            }
        });
    
}


function compose(){
    //document.querySelector('#all-posts-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    popify('#compose-view')
}

// avoid user sending empty posts
document.querySelector('#compose-body').addEventListener('keyup', function (){
    if(this.value.length > 1){
        document.querySelector('#compose-submit').disabled = false;
    }else{
        document.querySelector('#compose-submit').disabled = true;

    }
})


// send post to server
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
        document.location.href="/"
    });
    }
    



})
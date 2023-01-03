document.addEventListener('DOMContentLoaded', function() {

let user_profiling = document.querySelector('#u_name').value;
let request_user = document.getElementById('request_user').value;

//fetch for profile infos from server
get_infos( String(user_profiling))

function get_infos(user){
    console.log('start fetching from server')
    fetch(`/${user}/infos`)
    .then(response => response.json())
    .then(infos => {
        // Print emails
        console.log(infos);
        user_id = infos['id']
        user_first_name = infos['first_name']
        user_last_name = infos['last_name']
        user_email = infos['user_email']
        user_joined_date = infos['date_joined']
        user_num_posts = infos['num_posts']
        user_posts = infos['post_objects']
        is_followed_by_current_user = infos['following']

        follow_button = document.querySelector('#follow_btn')


        if (request_user == user_id){
            follow_button.style.display ='none';
        }

        if (is_followed_by_current_user){
            follow_button.innerHTML = "Unfollow"
            change = "follow"
        }else {
            follow_button.innerHTML = "follow"
            change = "unfollow"
        }


        //update user infos
        //update first and last name
        document.querySelector('#user_profile_name').innerHTML = `${user_first_name} ${user_last_name}`

        //update email
        document.querySelector('#user_profile_mail').innerHTML = `${user_email}`
        document.querySelector('#user_profile_joined_date').innerHTML = `${user_joined_date}`
        document.querySelector('#user_profile_num_posts').innerHTML = `${user_num_posts}`

        for (post of user_posts){
            post_user = post['user']
            post_timestamp = post['timestamp']
            post_id = post['id']
            post_body = post['body']
            post_num_likes = post['likes']


            post_container = document.createElement('div');
            post_container.id = `post-container-${post_id}`
            post_container.className += "tweet_container"
            post_container.innerHTML = `

            <div class="image_container">
            <img  src="https://i.imgur.com/0PmI3ZD.png" alt="" srcset="">                    
            </div>


            <div class="tweet_body_container" >
                <div class="tweet_header_container">
                    <span class="tweet_username" >${post_user}</span>  <span class="tweet_user_at" >${post_user}</span> <span class="tweet_date">${post_timestamp}</span>

                </div>
                <div class="tweet_body_text">
                    <p id="tweet_body_text">
                       ${post_body}
                    </p>
                </div>
                <div class="tweet_footer">
                    <div class="tweet_footer_item">
                        <span>
                            <i class="fa-regular fa-heart"></i>
                        </span>
                        <p> ${post_num_likes}</p>
                    </div>

                </div>
            </div>
            
            `

            document.querySelector('#toggle_view_container').appendChild(post_container)

        }
        // follow and unfollow 
        follow_button.addEventListener('click', function (){

            fetch('/follow', {
                method: 'PUT',
                body: JSON.stringify({
                    followed_user: user_id,
                    action : "unfollow",
                    user : request_user
                })
            })
            .then(response => {
                console.log('following done')
            })

        })
    });
}




})
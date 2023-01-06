// wait for the DOm content to load
document.addEventListener('DOMContentLoaded', function (){
// by default load new post
console.log('index js running here')

localStorage.setItem("current_section", 1)
current_local_storage_page = localStorage.getItem("current_section")

var user_exist = document.querySelector('#profiled_user_name') 
if (user_exist){
    console.log('user exists on this page')
    load_post(user_exist.value, current_local_storage_page)

}else {
    document.querySelector('#all-posts-view').style.display = 'block';
    load_post("all", current_local_storage_page)
    console.log('calling loadpost all')
}





// on headers click
document.querySelector('#all-posts').addEventListener('click', () => load_post('all',1))
document.querySelector('#add-post').addEventListener('click', () => compose())
document.querySelector('#Following').addEventListener('click', () => load_post('following', 1) )


// overlay fonctions
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

// load posts from server

function load_post(which, section){
    console.log(`called with ${which}`)

        // hide other view
        if (which == "all" || which == "following"){
            console.log('load post called with all or following')
            document.querySelector('#all-posts-view').style.display = 'block';
            document.querySelector('#compose-view').style.display = 'none';
            main_container = document.querySelector('#all-posts-view')
        }else {
            main_container = document.querySelector('#toggle_view_container')
        }


        main_container.innerHTML = ''

        pagination_page = document.querySelector('.pagination')
        pagination_page.innerHTML=''

        //fetch for the posts
        fetch(`/posts/${which}/${section}`)
        .then(response => response.json())
        .then(posts => {
            console.log(posts)

            for (const post of posts['posts']){
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
                        <span class="tweet_username"> <a href="${post_user}/profile"> <p> ${post_user} </p> </a> </span>  <span class="tweet_user_at" >SudoOverloord</span> <span class="tweet_date">${post_timestamp}</span>

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

                main_container.append(post_container)   
                document.querySelector('#pagination_nav').style.display = "block";
            }

            // 
            previous_page = document.createElement('li')
            previous_page.className += "page-item"
            previous_page.innerHTML = '<a class="page-link" data-section="-1" href="#">Previous</a>'
            listen_to_load(previous_page, which)

            next_page = document.createElement('li')
            next_page.className += "page-item"
            next_page.innerHTML = '<a class="page-link" data-section="+1" href="#">Next</a>'
            listen_to_load(next_page, which)

            if (section == 1){
                previous_page.style.display = "none"
            }

            if (section == parseInt(posts['num_pages'])){
                next_page.style.display = "none"
            }

            pagination_page.append(previous_page)
            
            for (let i = 1; i < parseInt(posts['num_pages'])+1; i++){
                let num = document.createElement('li')
                num.innerHTML=`<a class="page-link" data-section="${i}" href="#">${i}</a>`
                num.className += "page-item"
                num.firstElementChild.setAttribute("id",`page_link_${i}`)
                listen_to_load(num, which)

                pagination_page.append(num)
            }
            pagination_page.append(next_page)


            document.querySelector(`#page_link_${section}`).style.backgroundColor = "#6649b8"




            return false
        });


}

// function_load_from_page_menu
function listen_to_load(args, which){
    args.firstElementChild.addEventListener('click', function(){

        stored_section = localStorage.getItem("current_section")
        console.log(this.dataset.section)

        if (this.dataset.section == "-1"){
            current_section = parseInt(stored_section) - 1
            if (current_section < 1){current_section = 1}
            localStorage.setItem("current_section", current_section)
            console.log(`stored_section is ${stored_section} current is ${current_section}`)
            load_post(which, current_section)

        }else if (this.dataset.section == "+1"){
            current_section = parseInt(stored_section) + 1
            localStorage.setItem("current_section", current_section)
            console.log(`stored_section is ${stored_section} current is ${current_section}`)
            load_post(which, current_section)
        }
        else{
            localStorage.setItem("current_section", this.dataset.section)

            load_post(which,this.dataset.section) 
        }
    })
}

// show compose form for new post

function compose(){
    //document.querySelector('#all-posts-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'block';
    popify('#compose-view')
}

// avoid user sending empty posts
document.querySelector('#compose-body').addEventListener('keyup', function (){
    if(this.value.length > 0){
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

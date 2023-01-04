document.addEventListener('DOMContentLoaded', function() {

Follow_button = document.querySelector('#follow_btn');
profiled_user = document.querySelector('#profiled_user').value;
current_user = document.querySelector('#request_user').value;

// go bzck when back span clicked
document.querySelector('#profile_back_arrow').addEventListener('click', function(){
    history.go(-1);
})


// avoid user to follow itself
if (profiled_user == current_user){
    Follow_button.style.display = "none";
}

profiled_user_name = document.querySelector('#profiled_user_name').value;
Follow_button.addEventListener('click', function() {


    console.log(profiled_user)

    fetch('/follow', {
        method: 'PUT',
        body: JSON.stringify({
            followed_user : profiled_user,
            followed_user_name : profiled_user_name,
            action : Follow_button.innerHTML
        })
      })
    .then(result => {
        window.location.reload();
    });
        
})



})
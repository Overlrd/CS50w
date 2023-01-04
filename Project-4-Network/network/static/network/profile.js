document.addEventListener('DOMContentLoaded', function() {

Follow_button = document.querySelector('#follow_btn');
Follow_button.addEventListener('click', function() {
    profiled_user = document.querySelector('#profiled_user').value;
    profiled_user_name = document.querySelector('#profiled_user_name').value;

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
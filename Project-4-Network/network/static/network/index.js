// wait for the DOm content to load
document.addEventListener('DOMContentLoaded', function (){
    console.log('dom loaded')
// on headers click
document.querySelector('#all-posts').addEventListener('click', () => {
    // do something here
})


// function write post
document.querySelector('#compose-form').onsubmit = () => {
    const body = document.querySelector('#compose-body').value;
    // pass a post request to the backend
    fetch('/new_post', {
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
document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email(null));

  // By default, load the inbox
  load_mailbox('inbox');

  // on compose form submit
  document.querySelector('#compose-form').onsubmit = () => {
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;
    // pass a post request to the backend
    fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
    })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        alert(`${result}`)
    });
  }


});


function animate(){
  element = document.querySelector('#emails-view');
  element.style.animationPlayState = 'running';
}

 
function compose_email(recipients, subject, timestamp, body) {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#mail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  if (recipients == null && subject == null){


  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}else{
  document.querySelector('#compose-recipients').value = `${recipients}`;
  console.log(`compose called with recipient ${recipients},${subject},${body} `)

  if(subject.includes('Re')){
    document.querySelector('#compose-subject').value = `${subject}`;
  }else{
    document.querySelector('#compose-subject').value = `Re :${subject}`;

  }
  // pre-fill the body
  document.querySelector('#compose-body').value = `On ${timestamp} ${recipients} wrote ${body}`;

}


}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#mail-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';

  document.getElementById("emails-view").classList.remove("div_to_animate");
  document.getElementById("emails-view").classList.add("div_to_animate");


  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)} </h3>`;

  // API request for the mailbox content
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {

      // ... do something else with emails ...
      for (const email of emails){
        // extracting mail infos to display
        mail_subject = email['subject']
        mail_recipients = email['recipients']
        mail_date = email['timestamp']
        mail_sender = email['sender']
        mail_id = email['id']
        
        mail_container = document.createElement('div');
        mail_container.id =`mail-container${mail_id}`;
        mail_container.className += "mail_container";
        
        // styling the new div
        mail_container.style.border = '1px solid black';
        mail_container.style.display = 'flex';
        mail_container.style.alignItems = 'center';
        mail_container.style.justifyContent = 'space-between';
        
        // hover 
        mail_container.addEventListener('mouseover', function(){
          this.style.cursor = 'pointer';
        })


        if (mailbox == 'inbox'){
          mail_container.innerHTML = `<div style='margin:10px; font-weight:bold;'>Id : ${mail_id} From : ${mail_sender}</div> <div style='margin:10px;'>Subject : ${mail_subject}</div> <div class='.navbar-text' style='margin:10px;'>${mail_date}</div>`;
          to_archive = true ;

          //update notif bail


        } else {
          mail_container.innerHTML = `<div style='margin:10px; font-weight:bold;'>Id : ${mail_id} To : ${mail_recipients}</div> <div style='margin:10px;'>Subject : ${mail_subject}</div> <div class='.navbar-text' style='margin:10px;'>${mail_date}</div>`;
          to_archive = false ;

        }

        // style readed and unreaded messages
        if (email['read']){
          mail_container.style.backgroundColor = 'white'; 
        }else {
          mail_container.style.backgroundColor = 'gray'; 
          mail_container.style.color = 'white'; 
        }

        document.querySelector('#emails-view').appendChild(mail_container)

      } 

      // view a specific mail
      for (const email of emails){
        // get each mail's div
        const email_id = email['id']
        current_div = document.querySelector(`#mail-container${email_id}`)
        current_div.addEventListener('click', function(){
          console.log(`${email_id}']} clicked `)
          console.log(`called load_email ( ${email_id} , ${mailbox})`)
          load_email(email_id,mailbox)
        })
      }
  });
}

function load_email(email_id, mailbox){
    // Show the mail view and hide other views
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#mail-view').style.display = 'block';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#mail-button-archive').style.display = 'none';


    if (mailbox == 'inbox'){
      console.log('mailbox is inbox')
      document.querySelector('#mail-button-archive').style.display = 'unset';
    }else if (mailbox == 'archive'){
      document.querySelector('#mail-button-archive').style.display = 'unset';
      document.querySelector('#mail-button-archive').innerHTML = 'Unarchive';
    }

    // API request for the mailbox content
    fetch(`/emails/${email_id}`)
    .then(response => response.json())
    .then(email => {
      console.log(email)
      console.log(mailbox)
      // extract email's infos
      const id = email['id']
      const sender = email['sender']
      const recipients = email['recipients']
      const subject = email['subject']
      const timestamp = email['timestamp']
      const body = email['body']

      // update mail view values 
      document.querySelector('#mail-sender').innerHTML = `From : ${sender}`;
      document.querySelector('#mail-receiver').innerHTML = `To : ${recipients}`;
      document.querySelector('#mail-subject').innerHTML = `Subject: ${subject}`;
      document.querySelector('#mail-content').innerHTML = `${body}`;
      document.querySelector('#mail-time').innerHTML = `Timestamp: ${timestamp}`;

      // update read status
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })

        // reply 
        document.querySelector('#mail-button-reply').addEventListener('click', function(){
          compose_email(sender, subject, timestamp, body)
        })

      // archive & unarchive

      document.querySelector('#mail-button-archive').addEventListener('click', function(){
      console.log('archive button clicked')
      fetch(`/emails/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            archived: to_archive
        })
      })
      .then(
        document.location.href="/"
      )

      
    })

    })


}


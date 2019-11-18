(function(){
  let signInForm = document.getElementById('signInform');
  let alertErrors = document.getElementById('errors');
  let submit = signInForm.getElementsByTagName('button')[0];
  
  signInForm.addEventListener('submit', function(event){
    submit.disabled = true; // block double submit or clic
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;
    
    event.preventDefault(); // avoid default behavior
    
    let data = new URLSearchParams();
    data.append('username', username);
    data.append('password', password);
    
    axios({
      method: 'post',
      url: urlSignIn,
      data: data,
      xsrfCookieName: 'csrftoken',
      xsrfHeaderName: 'X-CSRFToken',
      headers: {
        'cache-control':  'no-cache',
        'content-type':   'application/x-www-form-urlencoded'
        }
    })
    .then(function (response) {
      if (response.status === 200) {
        alertErrors.hidden = true;
        window.location.replace('../');
      }
    })
    .catch(function (error) {
      alertErrors.innerHTML = ''
      let strError = '';
      let errors = JSON.parse(error.response.data);

      for (var err in errors) {
        strError += '<p>' + errors[err] + '</p>';   
      }
      
      alertErrors.innerHTML = strError;
      alertErrors.removeAttribute('hidden');
      submit.disabled = false;
    });
  });
})();

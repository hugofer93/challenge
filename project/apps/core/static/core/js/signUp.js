(function(){
    let signUpForm = document.getElementById('signUpform');
    let alertErrors = document.getElementById('errors');
    let submit = signUpForm.getElementsByTagName('button')[0];
    
    signUpForm.addEventListener('submit', function(event){
        submit.disabled = true; // block double submit or clic

        let username = document.getElementById('username').value;
        let firstName = document.getElementById('first_name').value;
        let lastName = document.getElementById('last_name').value;
        let email = document.getElementById('email').value;
        let password1 = document.getElementById('password1').value;
        let password2 = document.getElementById('password2').value;

        event.preventDefault(); // avoid default behavior

        let data = new URLSearchParams();
        data.append('username', username);
        data.append('first_name', firstName);
        data.append('last_name', lastName);
        data.append('email', email);
        data.append('password1', password1);
        data.append('password2', password2);

        axios({
            method: 'post',
            url: urlSignUp,
            data: data,
            xsrfCookieName: 'csrftoken',
            xsrfHeaderName: 'X-CSRFToken',
            headers: {
              'cache-control':  'no-cache',
              'content-type':   'application/x-www-form-urlencoded'
              }
        })
        .then(function (response) {
          if (response.status === 201) {
            alertErrors.hidden = true;
            window.location.replace('../');
          }
        })
        .catch(function (error) {
            alertErrors.innerHTML = ''
            let strError = '';
            let errors = JSON.parse(error.response.data);
            
            for (var err in errors) {
              for (var e in errors[err]) {
                strError += '<p>' + err + ': ' + errors[err][e] + '</p>';
              }   
            }
            
            alertErrors.innerHTML = strError;
            alertErrors.removeAttribute('hidden');
            submit.disabled = false;
        });

    });
    
})();

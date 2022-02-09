function validate() {
        var username = document.getElementById("username").value;
        var password = document.getElementById("password").value;
        if (username == null || username == "") {
            document.getElementById('myError').text('Please enter a username')
            return false;
        }
        if (password == null || password == "") {
            document.getElementById('myError').text('Please enter a password')

            return false;
        }
        return true;

    }
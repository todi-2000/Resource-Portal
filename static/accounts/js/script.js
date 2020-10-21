// Scrolling effect and Swap Handler
$('.foot-var').on('click', function () {
    if (this.textContent == 'student\'s') {
        $(this).text('teacher\'s');
        $('.login-teacher').slideUp();
        // $('.hero').delay(200).css({ "background-image": "url(../img/student-bg.jpg)" });
        $('.login-student').delay(400).slideDown();

    }
    else {
        $(this).text('student\'s');
        $('.login-student').slideUp();
        // $('.hero').css({ "background-image": "url(../img/black.jpg)" });
        $('.login-teacher').delay(400).slideDown();
    }
});

// Password Toggle Handler
$('.shift-student').on('click', function () {
    $(this).toggleClass('fa-eye-slash');

    let studentpass = document.getElementById('s_pass');
    (studentpass.type == 'password') ? (studentpass.setAttribute("type", "text")) : (studentpass.setAttribute("type", "password"));
});

$('.shift-teacher').on('click', function () {
    $(this).toggleClass('fa-eye-slash');

    let teacherpass = document.getElementById('t_pass');
    (teacherpass.type == 'password') ? (teacherpass.setAttribute("type", "text")) : (teacherpass.setAttribute("type", "password"));
});

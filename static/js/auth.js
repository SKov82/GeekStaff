'use strict'

// Прячет чекбокс персональных данных для работодателя и показывает его для соискателя

const agree = document.querySelector('.agree'),
    role = document.getElementById('id_role')

if (role) {
    role.addEventListener('click', () => {
        if (role.value === 'HR') {
            agree.innerHTML = ''
        } else {
            agree.innerHTML = `
                <input type="checkbox" name="agree" id="agree" required>
                <label for="agree">Согласен на публикацию персональных данных</label>
            `
        }
    })
}


// При клике по глазу скрывает / раскрывает пароль

const eye = document.querySelectorAll('.ti-eye')

eye.forEach(el => {
    el.addEventListener('click', () => {
        const pass = el.parentElement.previousElementSibling

        if (pass.type === 'password') {
            pass.type = 'text'
        } else {
            pass.type = 'password'
        }
    })
})
const button = document.getElementById('submit')

button.addEventListener('click', run)


function run() {
    event.preventDefault()
    let sk = document.getElementById('sk')
    const laimingas = 5<=sk<=10 || 20<=sk<=25
    if (laimingas) {
        console.log('Laimingas')
    }
    else {
        console.log('Nelaimingas')
    }
}
window.onload = () => {
    document.querySelector('#id_file_order').oninput = () =>{
        let input = document.querySelector('#id_file_order');

        document.querySelector('#add-file-p').style.display = 'flex';
        document.querySelector('#add-file-p p').innerHTML = input.value.slice(input.value.lastIndexOf('\\') + 1);
    }
}
function processTaskData(identifier) {
    const taskId = $(identifier).data('id');
    const taskTitle = $(identifier).data('title');
    const modalTitle = 'Удалить выбранную задачу <i>' + taskTitle + '</i>?'
    const url = '/tasks/' + taskId + '/delete'
    //console.log(modalTitle, url)
    document.getElementById('myModalLabel').innerHTML = modalTitle
    document.getElementById('deleteButton').addEventListener("click", () => {
        window.location = url;
    });
}
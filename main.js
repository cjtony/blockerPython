
document.addEventListener('DOMContentLoaded', () => {

	const btnInit = document.getElementById('btnInit');

	eventListener = () => {
		btnInit.addEventListener('click', () => {
			paintConsol();
		});
	}

	paintConsol = () => {
		console.log('Hola');
	}

	/*
		Funcion Principal
	*/

	eventListener();

});
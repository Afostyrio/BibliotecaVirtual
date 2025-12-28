$(document).ready(function(){
	const currentDate = new Date();

	const lightrope = document.getElementById('lightrope');
	console.log(currentDate)

	if (currentDate.getMonth() === 11) {
	lightrope.style.display = 'block';
	}
})
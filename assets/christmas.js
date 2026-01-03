$(document).ready(function(){
	const currentDate = new Date();

	const lightrope = document.getElementById('lightrope');
	console.log(currentDate)

	const currentMonth = currentDate.getMonth()
	if (currentMonth === 10|| currentMonth === 11 || currentMonth === 0) {
	lightrope.style.display = 'block';
	}
})
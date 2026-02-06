---
title: Olimpiada de Otoño
urlname: olimpiada-otono
logo-title: ../assets/img/Logo-carma.png
layout: home
altname: La ancestral Olimpiada de Otoño
---

  <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
  {% assign nacionales = site.data.nacionales_carma.otono | sort: "year"%}
  {% for nacional in nacionales reversed%}
	  <div class="col">
		<div class="card h-100 mb-3">
		  <a
			href="{{site.baseurl}}/assets/pdf/CARMA/Otono/{{nacional.year}}.pdf"
			target="_blank"
			rel="noopener noreferrer"
		  >
			<img
			  height="150px"
			  style="object-fit: contain;"
			  class="card-img-top border-bottom bg-white"
			  src="{{site.baseurl}}/assets/img/{{nacional.thumbnail}}"
			  alt="Olimpiada de Otoño {{ nacional.year }}">
		  </a>
		  <div class="card-body">
			<a
			  href="{{site.baseurl}}/assets/pdf/CARMA/Otono/{{nacional.year}}.pdf"
			  target="_blank"
			  class="card-link"
			  rel="noopener noreferrer"
			>Olimpiada de Otoño {{ nacional.year }}</a>
		  </div>
		</div>
	  </div>
  {% endfor %}
  </div>

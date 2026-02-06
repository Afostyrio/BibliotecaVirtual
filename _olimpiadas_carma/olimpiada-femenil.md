---
title: Olimpiada Femenil
urlname: olimpiada-femenil
logo-title: ../assets/img/Logo-carma.png
layout: home
altname: La original Olimpiada Femenil
---

  <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
  {% assign nacionales = site.data.nacionales_carma.femenil | sort: "year"%}
  {% for nacional in nacionales reversed%}
	  <div class="col">
		<div class="card h-100 mb-3">
		  <a
			href="{{site.baseurl}}/assets/pdf/CARMA/Femenil/{{nacional.year}}.pdf"
			target="_blank"
			rel="noopener noreferrer"
		  >
			<img
			  height="150px"
			  style="object-fit: contain;"
			  class="card-img-top border-bottom bg-white"
			  src="{{site.baseurl}}/assets/img/{{nacional.thumbnail}}"
			  alt="Olimpiada Femenil {{ nacional.year }}">
		  </a>
		  <div class="card-body">
			<a
			  href="{{site.baseurl}}/assets/pdf/CARMA/Femenil/{{nacional.year}}.pdf"
			  target="_blank"
			  class="card-link"
			  rel="noopener noreferrer"
			>Olimpiada Femenil {{ nacional.year }}</a>
		  </div>
		</div>
	  </div>
  {% endfor %}
  </div>

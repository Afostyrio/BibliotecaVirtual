---
title: Olimpiada Mexicana de Matemáticas para Educación Básica
urlname: ommeb
logo-title: ../assets/img/Logo-ommeb.png
layout: home
altname: OMMEB
---

{% for edition in site.data.nacionales.ommeb reversed %}
<div class="row">
	<div class="col mb-3">
	<h2 class="text-center" id="{{edition.year}}">{{edition.year}}</h2>
	<h3 class="text-center">{{edition.location}}</h3>
	{% for item in edition.modes %}
  <h3>{{item.mode}}</h3>
	{% assign label = item.mode | split: '' %}
  <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
	{% for level in item.levels %}
			<div class="col">
				<div class="card h-100 mb-3">
					<a
						href="{{site.baseurl}}/assets/pdf/Nacionales/OMMEB/{{edition.year}}-{{label[0]}}-N{{level.level}}.pdf"
						target="_blank"
						rel="noopener noreferrer"
					>
						<img
							height="150px"
							style="object-fit: contain;"
							class="card-img-top border-bottom bg-white"
							src="{{site.baseurl}}/assets/img/{{edition.thumbnail}}"
							alt="Nacional {{ edition.year }} Nivel {{level.level}} {{item.mode}}">
					</a>
					<div class="card-body">
						<a
							href="{{site.baseurl}}/assets/pdf/Nacionales/OMMEB/{{edition.year}}-{{label[0]}}-N{{level.level}}.pdf"
							target="_blank"
							class="card-link"
							rel="noopener noreferrer"
						>OMMEB {{ edition.year }} Nivel {{level.level}} {{item.mode}}</a>
					</div>
				</div>
			</div>
    {% endfor %}
    </div>
    {% endfor %}
  </div>
</div>
{% endfor %}
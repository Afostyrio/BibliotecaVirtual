---
title: Olimpiada Básica de Matemáticas
urlname: obmguanajuato
logo-title: ../assets/img/Logo.png
layout: home
altname: La poderosísima OBM
---

{% for edition in site.data.ediciones_obm reversed %}
<div class="row">
	<div class="col mb-3">
	<h2 class="text-center">{{edition.year}}</h2>
		<div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
		{% for item in site.selectivos_obm %}
			{% if item.year == edition.year %}
				<div class="col">
					<div class="card h-100 mb-3">
						<a
							href="{{ item.file | relative_url }}"
							target="_blank"
							rel="noopener noreferrer"
						>
							<img
								height="150px"
								style="object-fit: contain;"
								class="card-img-top border-bottom bg-white"
								src="{{ item.thumbnail | relative_url}}"
								alt="Selectivo {{ item.exam-number }}">
						</a>
						<div class="card-body">
							<a
								href="{{ item.file | relative_url }}"
								target="_blank"
								class="card-link"
								rel="noopener noreferrer"
							>Selectivo {{ item.exam-number }}</a>
							{{ item.year }}
						</div>
						<div class="card-footer text-body-secondary text-end">
							Nivel: {{ item.level }}
						</div>
					</div>
				</div>
			{% endif %}
		{% endfor %}
		</div>
	</div>
</div>
{% endfor %}


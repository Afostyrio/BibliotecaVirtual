---
title: Concurso Nacional Femenil de la Olimpiada Mexicana de Matemáticas
urlname: cnfomm
logo-title: ../assets/img/Logo-cnfomm.png
layout: home
---
{% for edition in site.data.nacionales.cnfomm reversed %}
<div class="row">
	<div class="col mb-3">
	<h2 class="text-center">{{edition.year}}</h2>
	<h3 class="text-center">{{edition.location}}</h3>
    <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
    {% for exam in edition.exams %}
        <div class="col">
          <div class="card h-100 mb-3">
            <a
              href="{{site.baseurl}}/assets/pdf/Nacionales/CNFOMM/{{edition.year}}-{{exam.tag}}.pdf"
              target="_blank"
              rel="noopener noreferrer"
            >
              <img
                height="150px"
                style="object-fit: contain;"
                class="card-img-top border-bottom bg-white"
                src="{{site.baseurl}}/assets/img/{{edition.thumbnail}}"
                alt="Nacional {{ edition.year }} {{exam.mode}}">
            </a>
            <div class="card-body">
              <a
                href="{{site.baseurl}}/assets/pdf/Nacionales/CNFOMM/{{edition.year}}-{{exam.tag}}.pdf"
                target="_blank"
                class="card-link"
                rel="noopener noreferrer"
              >Nacional {{ item.year }} {{exam.mode}}</a>
            </div>
          </div>
        </div>
    {% endfor %}
    </div>
  </div>
</div>
{% endfor %}
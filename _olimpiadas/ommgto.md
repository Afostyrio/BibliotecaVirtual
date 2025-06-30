---
title: Olimpiada Mexicana de Matemáticas
logo-title: ../assets/img/Logo-ommgto.png
urlname: ommgto
layout: home
altname: La poderosísima OMMGto
---

{% for edition in site.data.selectivos.ommgto reversed %}
<div class="row">
  <div class="col mb-3">
  <h2 class="text-center">{{edition.year}}</h2>
      <div class="row row-cols-1 row-cols-xl-4 row-cols-md-3 g-4">
      {% for exam in edition.exams %}
        <div class="col">
            <div class="card h-100 mb-3">
                <a
                    href="{{site.baseurl}}/assets/pdf/Selectivos/OMM/{{exam.file}}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    <img
                        height="150px"
                        style="object-fit: contain;"
                        class="card-img-top border-bottom bg-white"
                        src="{{site.baseurl}}/assets/img/{{edition.thumbnail}}"
                        alt="Selectivo {{exam.number}}">
                </a>
                <div class="card-body">
                    <a
                        href="{{site.baseurl}}/assets/pdf/Selectivos/OMM/{{exam.file}}"
                        target="_blank"
                        class="card-link"
                        rel="noopener noreferrer"
                    >Selectivo {{exam.number}}</a>
                    {{ edition.year }}
                </div>
            </div>
        </div>
      {% endfor %}
      </div>
  </div>
</div>
{% endfor %}


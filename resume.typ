#import "@preview/cmarker:0.1.6"

#set text(font: "Helvetica Neue")
#show heading.where(level: 1): set text(size: 22pt, weight: 800)
#set page(margin: (
  top: 1.5cm,
  bottom: 1cm,
  left: 1.5cm,
  right: 1.5cm,
))
// #set align(horizon)
#set text(size: 10.5pt)
#let blue = rgb(53, 116, 234)
#let green = rgb(67, 187, 117)
#show link: set text(blue)
#let gray(str) = text(rgb(130, 130, 130), str)
#let text_primary(str) = text(rgb("#0f172a"), str)
#let text_secondary(str) = text(rgb("#475569"), str)
#let text_muted(str) = text(rgb("#6b7280"), weight: "medium", str)
#set par(leading: 0.9em)

#let data = json("resume_" + sys.inputs.lang + ".json")
#let stats = json("data/pubs.json").stats
#let contact = json("data/contact.json")

#let render_item(item) = {
  // Convert Markdown to Typst using the built-in markdown function
  cmarker.render(item)
}

= #text(fill: gradient.linear(blue, green))[#data.name]
#v(2pt)
#text(size: 12pt, text_secondary(data.summary))
#v(-2pt)
#block()[
  #show link: set text(fill: rgb("#6b7280"), weight: "medium")
  #link("mailto:" + contact.mail)#h(5pt)#link(contact.github)[GitHub]#h(5pt)#link(contact.linkedin)[LinkedIn]
]

// #block(inset: 15pt)[
//   #set align(center)
//   #text(blue, weight: "medium", data.catch)
// ]
//
#block(fill: rgb("#f4f5f8"), inset: (left: 8pt, right: 8pt, top: 4pt, bottom: 4pt), radius: 4pt)[
  #set text(size: 10pt, weight: 400)
  #v(7pt)
  📄 #h(3pt) #stats.total #data.total_pubs_str, #stats.citations #data.total_citations_str.
  #v(-5pt)
  ⚙️ #h(3pt) #gray(render_item(data.technical_stack))
  #v(7pt)
]

== Experience

#block(inset: 10pt, for job in data.experience {
  text(size: 10.5pt, strong(job.title)) + "  " + text_muted(text(size: 10pt, render_item(job.location)))
  block(inset: (left: 5pt, top: 3pt, bottom: 3pt), for item in job.description {
    text(size: 10pt, list.item(render_item(item)))
    v(2pt)
  })
})

== Education

#block(inset: 10pt, for edu in data.education {
  strong(edu.degree) + ", " + text_muted(text(size: 10pt, edu.location)) + "\n"
})

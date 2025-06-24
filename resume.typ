#import "@preview/cmarker:0.1.6"

#set text(font: "Helvetica Neue")
#show heading.where(level: 1): set text(size: 22pt, weight: 800)
#set page(margin: (
  top: 2cm,
  bottom: 1cm,
))
#set text(size: 10.5pt)
#let blue = rgb(53, 116, 234)
#let green = rgb(67, 187, 117)
#show link: set text(blue)
#let gray(str) = text(rgb(130, 130, 130), str)
#set par(leading: 0.9em)

#let data = json("resume_" + sys.inputs.lang + ".json")
#let stats = json("data/pubs.json").stats
#let contact = json("data/contact.json")

#let render_item(item) = {
  // Convert Markdown to Typst using the built-in markdown function
  cmarker.render(item)
}

= #text(fill: gradient.linear(blue, green))[#data.name]
#text(size: 13pt, gray(data.summary))
#v(-6pt)
#block[
  #show link: set text(fill: rgb(130, 130, 130))
  #show link: underline
  #link("mailto:" + contact.mail) · #link(contact.github)[GitHub] · #link(contact.linkedin)[LinkedIn]
]

#v(7pt)
📄 #stats.total #data.total_pubs_str, #stats.citations #data.total_citations_str.
#v(-5pt)
⚙️ #gray(render_item(data.technical_stack))
#v(7pt)

== Experience

#block(inset: 10pt, for job in data.experience {
  strong(job.title) + "  " + gray(render_item(job.location))
  for item in job.description { list.item(render_item(item)) }
  v(4pt)
})

== Education

#block(inset: 10pt, for edu in data.education {
  strong(edu.degree) + ", " + gray(edu.location) + "\n"
})

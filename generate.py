from pathlib import Path
from html import escape
p=Path('public'); p.mkdir(exist_ok=True)
recipes=[
 dict(slug='lemon-chickpea-rice-bowls',title='Lemon Chickpea Rice Bowls',category='Weeknight dinners',time='30 minutes',servings='4 servings',intro='Warm rice, crisp cucumber and chickpeas tossed with a bright lemon dressing. This is an easy dinner that also packs well for lunch.',ingredients=['1 cup dry long grain rice','1 can (15 oz) chickpeas, drained and rinsed','1 cucumber, diced','1 cup cherry tomatoes, halved','1/4 red onion, finely diced','3 tablespoons olive oil','2 tablespoons fresh lemon juice','1 small garlic clove, grated','1/2 teaspoon ground cumin','1/4 cup chopped parsley','Salt and black pepper, to taste'],steps=['Rinse the rice until the water runs mostly clear. Cook it according to the package directions, then fluff with a fork and let it rest for 5 minutes.','Whisk the olive oil, lemon juice, garlic, cumin, 1/2 teaspoon salt and a few grinds of black pepper in a large bowl.','Add the chickpeas, cucumber, tomatoes and red onion. Toss well and let stand for 5 minutes so the chickpeas absorb the dressing.','Divide the warm rice between four bowls. Spoon the chickpea mixture over the top and finish with parsley. Taste and add more lemon or salt if needed.'],tips='For meal prep, keep the cucumber mixture separate from the rice and refrigerate in covered containers for up to 3 days. Serve cold or reheat only the rice.'),
 dict(slug='tomato-white-bean-skillet',title='Tomato & White Bean Skillet',category='One-pan meals',time='25 minutes',servings='4 servings',intro='A pantry-friendly skillet with soft white beans, garlicky tomatoes and greens. Serve it with toast to catch the sauce.',ingredients=['2 tablespoons olive oil','1 small yellow onion, diced','3 garlic cloves, thinly sliced','1 can (28 oz) crushed tomatoes','2 cans (15 oz each) cannellini beans, drained and rinsed','1 teaspoon dried oregano','1/4 teaspoon red pepper flakes (optional)','2 packed cups baby spinach','1 tablespoon lemon juice','Salt and black pepper, to taste','Crusty bread, to serve'],steps=['Warm the oil in a large skillet over medium heat. Add the onion and a pinch of salt. Cook for 5 minutes, stirring, until softened.','Add garlic, oregano and pepper flakes. Stir for 30 seconds, just until fragrant.','Pour in the tomatoes and add the beans. Simmer uncovered for 12 to 15 minutes, stirring occasionally, until the sauce thickens.','Fold in the spinach and cook for 1 to 2 minutes until wilted. Stir in lemon juice, season to taste and serve with bread.'],tips='If the sauce gets too thick, add a splash of water. Leftovers keep covered in the refrigerator for up to 3 days.'),
 dict(slug='apple-cinnamon-baked-oats',title='Apple Cinnamon Baked Oats',category='Breakfast',time='40 minutes',servings='6 servings',intro='Soft, warmly spiced oats with chunks of apple and a crisp golden top. Make a pan once and breakfast is ready for several mornings.',ingredients=['2 cups old-fashioned rolled oats','1 teaspoon baking powder','1 1/2 teaspoons ground cinnamon','1/4 teaspoon salt','2 cups milk or unsweetened oat milk','1 large egg','1/4 cup maple syrup','2 tablespoons melted butter or neutral oil','1 teaspoon vanilla extract','2 medium apples, cored and diced','1/3 cup chopped walnuts (optional)'],steps=['Heat the oven to 350°F (175°C). Lightly grease an 8-inch square baking dish.','Mix oats, baking powder, cinnamon and salt in a large bowl. In another bowl whisk milk, egg, maple syrup, melted butter and vanilla.','Stir the wet mixture into the oats. Fold in most of the apple, then pour into the baking dish. Scatter the remaining apple and walnuts over the top.','Bake for 30 to 35 minutes until the center is set and the edges are golden. Rest for 10 minutes before cutting into six portions.'],tips='Refrigerate covered for up to 4 days. Reheat individual portions with a splash of milk. Use certified gluten-free oats when needed.'),
 dict(slug='crispy-sheet-pan-potatoes',title='Crispy Sheet-Pan Potatoes',category='Sides',time='45 minutes',servings='4 servings',intro='Golden edges, fluffy centers and a simple garlic-herb finish. The trick is giving the potatoes plenty of space on a hot pan.',ingredients=['1 1/2 lb (680 g) Yukon Gold potatoes','2 tablespoons olive oil','3/4 teaspoon kosher salt','1/2 teaspoon smoked paprika','1/4 teaspoon black pepper','1 garlic clove, finely grated','2 tablespoons chopped fresh parsley'],steps=['Heat the oven to 425°F (220°C). Place a large metal baking sheet in the oven while it heats.','Cut the potatoes into roughly 1-inch pieces. Dry them thoroughly with a clean towel, then toss with olive oil, salt, paprika and pepper.','Carefully spread the potatoes on the hot pan in a single layer with space between pieces. Roast for 20 minutes without disturbing them.','Flip the potatoes and roast another 15 to 20 minutes until browned and tender. Toss with garlic and parsley as soon as they leave the oven. Serve hot.'],tips='Drying the potatoes and leaving space between pieces helps them brown. Store leftovers refrigerated for up to 3 days and reheat in a hot oven.')]

recipes += [
 dict(slug='creamy-lemon-orzo',title='Creamy Lemon Orzo with Peas',category='Weeknight dinners',time='25 minutes',servings='4 servings',intro='A bright one-pot pasta with sweet peas, lemon and Parmesan. The orzo releases starch as it cooks, making a silky sauce without cream.',ingredients=['1 tablespoon olive oil','2 tablespoons butter','2 garlic cloves, minced','1 1/2 cups dry orzo','3 cups low-sodium vegetable broth','1 cup frozen peas','1 lemon, zest and 2 tablespoons juice','1/2 cup finely grated Parmesan','1/4 teaspoon black pepper','Salt, to taste'],steps=['Heat oil and butter in a large deep skillet over medium heat. Add garlic and stir for 30 seconds.','Add orzo and stir for 1 minute to coat the pasta. Pour in the broth, bring to a gentle simmer and cook uncovered for 10 to 12 minutes, stirring often, until the orzo is tender. Add a splash of water if the pan looks dry before the pasta is cooked.','Stir in frozen peas and cook for 2 minutes until hot. Turn off the heat and stir in lemon zest, juice, Parmesan and pepper.','Let stand for 2 minutes to thicken. Taste and season with salt. Serve immediately.'],tips='Orzo thickens as it cools. Reheat leftovers with a little water or broth; refrigerate for up to 3 days.'),
 dict(slug='banana-oat-pancakes',title='Banana Oat Pancakes',category='Breakfast',time='20 minutes',servings='8 small pancakes',intro='Tender oat pancakes made in a blender with ripe banana. Serve with yogurt, berries or a small drizzle of maple syrup.',ingredients=['1 cup old-fashioned rolled oats','1 ripe banana','2 large eggs','1/3 cup milk','1 teaspoon baking powder','1/2 teaspoon ground cinnamon','1 teaspoon vanilla extract','Pinch of salt','Butter or oil, for the pan'],steps=['Blend oats until they resemble coarse flour. Add banana, eggs, milk, baking powder, cinnamon, vanilla and salt. Blend until mostly smooth, then rest the batter for 5 minutes.','Lightly grease a nonstick skillet over medium-low heat. Spoon about 3 tablespoons of batter per pancake onto the pan.','Cook for 2 to 3 minutes until the edges look set and bubbles appear. Flip carefully and cook another 1 to 2 minutes until golden and cooked through.','Repeat with remaining batter, adjusting the heat if pancakes brown too quickly. Serve warm.'],tips='The batter thickens as it rests; loosen with a tablespoon of milk if needed. Refrigerate cooked pancakes for up to 3 days.'),
 dict(slug='honey-yogurt-berry-cups',title='Honey Yogurt Berry Cups',category='Desserts',time='15 minutes',servings='4 servings',intro='A no-bake dessert with thick yogurt, fresh berries, toasted oats and honey. Assemble just before serving to keep the topping crisp.',ingredients=['2 cups plain thick Greek yogurt','2 tablespoons honey, plus more to serve','1 teaspoon vanilla extract','2 cups mixed berries, washed and dried','1/2 cup rolled oats','2 tablespoons chopped almonds','Pinch of ground cinnamon'],steps=['Add oats and almonds to a dry skillet over medium heat. Toast for 4 to 5 minutes, stirring frequently, until fragrant and lightly golden. Remove from heat and mix with cinnamon.','Stir yogurt, honey and vanilla together in a bowl. Taste and adjust the honey if your berries are tart.','Spoon yogurt into four small glasses. Add berries and finish with the toasted oat mixture.','Drizzle lightly with honey and serve straight away.'],tips='Toast the oats ahead and store them airtight at room temperature for up to 3 days. Keep yogurt and berries chilled until serving.'),
 dict(slug='roasted-carrot-tahini-salad',title='Roasted Carrot & Tahini Salad',category='Sides',time='35 minutes',servings='4 servings',intro='Warm roasted carrots with a lemon-tahini dressing and parsley. A flavorful side for grains, beans or grilled mains.',ingredients=['1 1/2 lb (680 g) carrots, peeled','2 tablespoons olive oil','1/2 teaspoon ground cumin','1/2 teaspoon salt','2 tablespoons tahini','1 1/2 tablespoons lemon juice','2 to 3 tablespoons water','1 small garlic clove, grated','2 tablespoons chopped parsley'],steps=['Heat oven to 425°F (220°C). Cut carrots lengthwise into similar-sized pieces so they roast evenly.','Toss carrots with olive oil, cumin and salt. Spread on a sheet pan in one layer and roast for 22 to 27 minutes, turning halfway, until browned at the edges and tender.','Whisk tahini, lemon juice and garlic. Add water one tablespoon at a time until the sauce is pourable, then taste and season.','Arrange warm carrots on a platter, spoon over dressing and sprinkle with parsley.'],tips='Keep extra dressing separately in the refrigerator for up to 3 days. Stir in a splash of water before serving.')]

css='''@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');:root{--ink:#202719;--green:#274738;--lime:#e2edb9;--paper:#fbfaf5;--line:#dddcd2}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 'DM Sans',Arial,sans-serif}a{color:inherit}header{border-bottom:1px solid var(--line);background:#fff}header .wrap{display:flex;align-items:center;justify-content:space-between;gap:20px;padding:20px 24px}.brand{font:700 25px/1.1 'Playfair Display',Georgia,serif;text-decoration:none;color:var(--green)}nav{display:flex;gap:24px;flex-wrap:wrap}nav a{text-decoration:none;font-weight:600;font-size:14px}nav a:hover,.text-link:hover{text-decoration:underline}.wrap{max-width:1120px;margin:auto;padding:0 24px}main{min-height:65vh}.hero{background:var(--green);color:#fff;padding:72px 0 76px}.eyebrow{text-transform:uppercase;letter-spacing:.15em;font-size:13px;font-weight:700;color:#a9d395}.hero h1{max-width:800px;font:600 clamp(42px,6vw,76px)/1.09 'Playfair Display',Georgia,serif;letter-spacing:-.035em;margin:15px 0 18px}.hero p{max-width:620px;font-size:19px;color:#e9efdd}.section{padding:60px 0}.section h2,.article h1,.page h1{font:600 clamp(36px,4vw,55px)/1.15 'Playfair Display',Georgia,serif;letter-spacing:-.025em;margin:0 0 14px}.section-intro{max-width:650px;color:#536054;margin-bottom:30px}.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}.card{display:block;border:1px solid var(--line);background:#fff;text-decoration:none;overflow:hidden;border-radius:12px;transition:transform .2s,box-shadow .2s}.card:hover{transform:translateY(-3px);box-shadow:0 12px 24px #1b352018}.art{height:230px;display:grid;place-items:center;background:var(--card-bg);color:var(--card-color);font:600 42px/1.1 'Playfair Display',Georgia,serif;padding:24px;text-align:center;letter-spacing:-.03em}.card-content{padding:24px}.meta{font-size:13px;text-transform:uppercase;letter-spacing:.09em;font-weight:700;color:#64775d}.card h3{font:600 29px/1.18 'Playfair Display',Georgia,serif;margin:10px 0}.card p{margin:0 0 16px;color:#536054}.text-link{font-weight:700;color:var(--green)}.article,.page{max-width:800px;margin:0 auto;padding:64px 24px 90px}.article .lead,.page .lead{font-size:20px;line-height:1.6;color:#4c594d}.article h2,.page h2{font:600 29px 'Playfair Display',Georgia,serif;margin:42px 0 12px}.article ul,.article ol{padding-left:24px}.article li{padding:5px 0}.recipe-facts{display:flex;gap:30px;flex-wrap:wrap;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin:30px 0}.recipe-banner{height:240px;border-radius:12px;display:grid;place-items:center;background:var(--card-bg);color:var(--card-color);font:600 45px 'Playfair Display',Georgia,serif;text-align:center;padding:20px}.note{background:#edf1dc;border-left:4px solid var(--green);padding:18px 22px;margin-top:40px}footer{background:#172d24;color:#e8eede;padding:42px 0}footer .wrap{display:flex;justify-content:space-between;gap:30px;flex-wrap:wrap}footer a{color:#e8eede;margin-right:18px}footer small{display:block;margin-top:12px;color:#bacaba}.back{font-weight:700;color:var(--green);text-decoration:none}.back:hover{text-decoration:underline}@media(max-width:640px){header .wrap{align-items:flex-start;flex-direction:column}nav{gap:14px}.hero{padding:52px 0}.hero p{font-size:17px}.grid{grid-template-columns:1fr}.art{height:190px}.section{padding:40px 0}.article,.page{padding-top:42px}.recipe-banner{height:180px;font-size:35px}}'''
(p/'style.css').write_text(css)
(p/'favicon.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#274738"/><path d="M13 34h38c-.9 12-8.4 19-19 19S13.9 46 13 34Z" fill="#f7efdb"/><path d="M14 34h36" stroke="#d9a46e" stroke-width="3" stroke-linecap="round"/><path d="M30 28c-3.5-6.5-2-12.5 2.5-16.5 1.2 6.5 5 11.5-2.5 16.5Z" fill="#dfe9b2"/><path d="M35 26c1.5-7 6.5-10.5 12.5-10-1 6.5-5.5 11.5-12.5 10Z" fill="#aacd84"/></svg>''')
def shell(title,desc,body):
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} | The Everyday Table</title><meta name="description" content="{escape(desc)}"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/style.css"></head><body><header><div class="wrap"><a class="brand" href="/" aria-label="The Everyday Table home"><img src="/favicon.svg" alt="" width="42" height="42"><span>The Everyday Table</span></a><nav aria-label="Main navigation"><a href="/">Recipes</a><a href="/about/">About</a><a href="/contact/">Contact</a></nav></div></header><main>{body}</main><footer><div class="wrap"><div><strong>The Everyday Table</strong><small>Simple recipes for real life.</small></div><div><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a></div></div></footer></body></html>'''
def write(route,content):
 d=p/route;d.mkdir(parents=True,exist_ok=True);(d/'index.html').write_text(content)
colors=[('#dae7bd','#274738'),('#e8d0af','#563a24'),('#ebdbb8','#503b2c'),('#d5dfba','#32432e')]
cards=''.join(f'''<a class="card" data-category="{escape(r['category'])}" data-search="{escape((r['title']+' '+r['intro']+' '+' '.join(r['ingredients'])).lower())}" href="/recipes/{r['slug']}/"><div class="art" style="--card-bg:{colors[i % len(colors)][0]};--card-color:{colors[i % len(colors)][1]}">{escape(r['title'])}</div><div class="card-content"><div class="meta">{r['category']} · {r['time']}</div><h3>{r['title']}</h3><p>{r['intro']}</p><span class="text-link">View recipe →</span></div></a>''' for i,r in enumerate(recipes))
write('',shell('Easy recipes for everyday cooking','Practical breakfast, dinner and side dish recipes with clear ingredients, timings and step-by-step directions.','<section class="hero"><div class="wrap"><div class="eyebrow">Cook something good today</div><h1>Good food, made for everyday life.</h1><p>Dependable recipes with familiar ingredients, clear steps and enough detail to make dinner feel easier.</p></div></section><section class="section wrap"><h2>Explore the recipes</h2><p class="section-intro">Pick a quick dinner, a make-ahead breakfast or a side dish for tonight.</p><div class="browse"><label for="recipe-search">Find a recipe</label><input id="recipe-search" type="search" placeholder="Search by name or ingredient" autocomplete="off"><div class="filters" role="group" aria-label="Filter by category"><button type="button" class="active" data-filter="all">All</button><button type="button" data-filter="Breakfast">Breakfast</button><button type="button" data-filter="Weeknight dinners">Dinners</button><button type="button" data-filter="One-pan meals">One-pan</button><button type="button" data-filter="Sides">Sides</button><button type="button" data-filter="Desserts">Desserts</button></div><p id="result-count" role="status" aria-live="polite"></p></div><div class="grid" id="recipe-grid">'+cards+'</div><p id="no-results" hidden>No recipes found. Try another search or category.</p><script src="/browse.js" defer></script></section>'))
for i,r in enumerate(recipes):
 ingredients=''.join('<li>'+escape(x)+'</li>' for x in r['ingredients']);steps=''.join('<li>'+escape(x)+'</li>' for x in r['steps']);bg,fg=colors[i % len(colors)]
 body=f'''<article class="article"><a class="back" href="/">← All recipes</a><p class="meta">{r['category']}</p><h1>{r['title']}</h1><p class="lead">{r['intro']}</p><p class="author-line">Written by <a href="/about/">Elba Adams</a> · Mexico</p><div class="recipe-facts"><span><strong>Total time:</strong> {r['time']}</span><span><strong>Yield:</strong> {r['servings']}</span></div><div class="recipe-actions"><a href="#recipe" class="action">Jump to recipe</a><button type="button" class="action" onclick="window.print()">Print recipe</button></div><div class="recipe-banner" style="--card-bg:{bg};--card-color:{fg}">{r['title']}</div><section id="recipe"><h2>Ingredients</h2><ul>{ingredients}</ul><h2>Method</h2><ol>{steps}</ol></section><div class="note"><strong>Storage &amp; helpful tip</strong><br>{r['tips']}</div></article>'''
 write('recipes/'+r['slug'],shell(r['title'],r['intro'],body))
 import json
 data={'@context':'https://schema.org','@type':'Recipe','name':r['title'],'description':r['intro'],'author':{'@type':'Person','name':'Elba Adams','url':'https://www.everydaytablekitchen.com/about/'},'image':'https://www.everydaytablekitchen.com/'+({'lemon-chickpea-rice-bowls':'chickpea','tomato-white-bean-skillet':'beans'}.get(r['slug'],r['slug']))+'.webp','recipeCategory':r['category'],'recipeYield':r['servings'],'totalTime':'PT'+r['time'].split()[0]+'M','recipeIngredient':r['ingredients'],'recipeInstructions':[{'@type':'HowToStep','text':step} for step in r['steps']]}
 target=p/'recipes'/r['slug']/'index.html';markup=target.read_text().replace('</head>','<script type="application/ld+json">'+json.dumps(data,ensure_ascii=False).replace('<','\\u003c')+'</script></head>');target.write_text(markup)
write('about',shell('About Elba Adams','Meet Elba Adams, the Mexico-based writer behind The Everyday Table.','<div class="page"><h1>Meet Elba Adams</h1><div class="author-profile"><img src="/elba-adams.webp" width="360" height="360" alt="Illustrated portrait of Elba Adams" loading="lazy"><div><p class="meta">Food writer · Mexico</p><p class="lead">Elba Adams shares approachable recipes for busy home cooks.</p><p>At The Everyday Table, she focuses on familiar ingredients, clear steps and practical tips that help make everyday meals easier.</p></div></div><h2>About The Everyday Table</h2><p>Each recipe aims to answer the questions that matter at the stove: what to buy, how long it takes, what to do in each step and how to store leftovers. The focus is on accessible ingredients and practical meals you can return to again.</p><p>Cooking times are estimates; appliances and ingredient sizes vary. Check that food is properly cooked and follow safe storage practices in your own kitchen.</p><h2>How recipes are presented</h2><p>Each page lists ingredients, numbered steps and practical notes on substitutions or storage. Photos illustrate the finished dish; your result may vary with ingredients and equipment.</p><h2>How to use this site</h2><p>Browse the <a href="/">recipe collection</a>, choose a dish and follow the ingredients and numbered steps. Notes at the end of each recipe offer storage or preparation tips.</p></div>'))
write('contact',shell('Contact','How to reach The Everyday Table about recipe feedback or site questions.','<div class="page"><h1>Contact</h1><p class="lead">Have a question about a recipe or spotted an error?</p><p>This site is being prepared for launch. A dedicated contact address will be added before the site opens publicly. Until then, please use the contact route provided by the site owner when they share this site with you.</p></div>'))
write('privacy',shell('Privacy Policy','Read how The Everyday Table handles visitor data, analytics, cookies and potential advertising.','<div class="page"><h1>Privacy Policy</h1><p>Last updated: September 23, 2026.</p><p>The Everyday Table does not ask visitors to create accounts or submit personal information through this site. Standard hosting infrastructure may process technical information such as IP address, browser type and access logs to deliver and protect the website.</p><h2>Cookies and advertising</h2><p>The site may display advertising in the future. If Google AdSense is added, Google and its partners may use cookies or similar technologies to serve and measure ads, including ads based on visits to this and other websites, subject to applicable consent requirements. You can learn about Google’s advertising practices and manage personalization in <a href="https://myadcenter.google.com/" rel="noopener noreferrer">My Ad Center</a>.</p><p>Any analytics or advertising services enabled later should be reflected in this policy and, where required, a consent choice before nonessential cookies are used. This version of the site does not embed advertising scripts.</p><h2>External links</h2><p>Links to other websites are governed by their own privacy policies. We do not control those websites.</p><h2>Questions</h2><p>See the <a href="/contact/">contact page</a> for the current contact status.</p></div>'))
write('terms',shell('Terms of Use','Terms for using The Everyday Table recipes and content.','<div class="page"><h1>Terms of Use</h1><p>Last updated: September 23, 2026.</p><p>Recipes and other material on The Everyday Table are provided for personal, informational use. You may cook from the recipes and share a link to a page. Please do not republish the full text or site design as your own.</p><p>Ingredient availability, allergens, cooking times and equipment vary. Review ingredients for your dietary needs, practice food safety and use your judgment when cooking.</p><p>We may update, correct or remove content as the site develops. External websites linked here are operated by their respective owners.</p></div>'))
(p/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://www.everydaytablekitchen.com/sitemap.xml\n')
urls=['']+['recipes/'+r['slug']+'/' for r in recipes]+['about/','contact/','privacy/','terms/']
(p/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>https://www.everydaytablekitchen.com/'+u+'</loc></url>' for u in urls)+'</urlset>')

# Keep image markup in the source generator so future content builds preserve it.
for route, text_label, image, alt in [
    ('', 'Lemon Chickpea Rice Bowls', 'chickpea.webp', 'Lemon chickpea rice bowl'),
    ('', 'Tomato & White Bean Skillet', 'beans.webp', 'Tomato and white beans'),
    ('recipes/lemon-chickpea-rice-bowls', 'Lemon Chickpea Rice Bowls', 'chickpea.webp', 'Lemon chickpea rice bowl'),
    ('recipes/tomato-white-bean-skillet', 'Tomato & White Bean Skillet', 'beans.webp', 'Tomato and white beans'),
    ('', 'Apple Cinnamon Baked Oats', 'apple-cinnamon-baked-oats.webp', 'Apple Cinnamon Baked Oats'),
    ('recipes/apple-cinnamon-baked-oats', 'Apple Cinnamon Baked Oats', 'apple-cinnamon-baked-oats.webp', 'Apple Cinnamon Baked Oats'),
    ('', 'Crispy Sheet-Pan Potatoes', 'crispy-sheet-pan-potatoes.webp', 'Crispy Sheet-Pan Potatoes'),
    ('recipes/crispy-sheet-pan-potatoes', 'Crispy Sheet-Pan Potatoes', 'crispy-sheet-pan-potatoes.webp', 'Crispy Sheet-Pan Potatoes'),
    ('', 'Creamy Lemon Orzo with Peas', 'creamy-lemon-orzo.webp', 'Creamy Lemon Orzo with Peas'),
    ('recipes/creamy-lemon-orzo', 'Creamy Lemon Orzo with Peas', 'creamy-lemon-orzo.webp', 'Creamy Lemon Orzo with Peas'),
    ('', 'Banana Oat Pancakes', 'banana-oat-pancakes.webp', 'Banana Oat Pancakes'),
    ('recipes/banana-oat-pancakes', 'Banana Oat Pancakes', 'banana-oat-pancakes.webp', 'Banana Oat Pancakes'),
    ('', 'Honey Yogurt Berry Cups', 'honey-yogurt-berry-cups.webp', 'Honey Yogurt Berry Cups'),
    ('recipes/honey-yogurt-berry-cups', 'Honey Yogurt Berry Cups', 'honey-yogurt-berry-cups.webp', 'Honey Yogurt Berry Cups'),
    ('', 'Roasted Carrot & Tahini Salad', 'roasted-carrot-tahini-salad.webp', 'Roasted Carrot & Tahini Salad'),
    ('recipes/roasted-carrot-tahini-salad', 'Roasted Carrot & Tahini Salad', 'roasted-carrot-tahini-salad.webp', 'Roasted Carrot & Tahini Salad'),
]:
    target=p/route/'index.html'
    markup=target.read_text()
    from html import escape as html_escape
    encoded=html_escape(text_label)
    markup=markup.replace(encoded+'</div>', f'<img src="/{image}" alt="{alt}" loading="lazy"></div>', 1)
    if route and '&' in text_label:
        markup=markup.replace(text_label+'</div>', f'<img src="/{image}" alt="{alt}" loading="lazy"></div>', 1)
    target.write_text(markup)

(p/'style.css').write_text(css + '''
/* Photo frames contain images without letting their intrinsic size push into card copy. */
.art,.recipe-banner{position:relative;overflow:hidden}
.art img,.recipe-banner img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.card-content{position:relative;background:#fff}
@media (prefers-reduced-motion:no-preference){
 .hero .wrap{animation:arrive .65s ease-out both}
 .card{animation:arrive .55s ease-out both}
 .card:nth-child(2){animation-delay:.08s}.card:nth-child(3){animation-delay:.16s}.card:nth-child(4){animation-delay:.24s}
 .card img{transition:transform .45s ease}
 .card:hover img{transform:scale(1.045)}
 @keyframes arrive{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
}
@media (prefers-reduced-motion:reduce){.card,.card img{animation:none;transition:none}}
''')

(p/'browse.js').write_text("""const input=document.querySelector('#recipe-search');const buttons=[...document.querySelectorAll('[data-filter]')];const cards=[...document.querySelectorAll('#recipe-grid .card')];const count=document.querySelector('#result-count');const empty=document.querySelector('#no-results');let active='all';function update(){const query=input.value.trim().toLocaleLowerCase();let shown=0;for(const card of cards){const match=(active==='all'||card.dataset.category===active)&&(!query||card.dataset.search.includes(query));card.hidden=!match;if(match)shown++}count.textContent=shown+' '+(shown===1?'recipe':'recipes')+' found';empty.hidden=shown!==0}input.addEventListener('input',update);for(const button of buttons)button.addEventListener('click',()=>{active=button.dataset.filter;for(const b of buttons){b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button))}update()});buttons.forEach(b=>b.setAttribute('aria-pressed',String(b.classList.contains('active'))));update();""")
(p/'style.css').write_text((p/'style.css').read_text()+"""
.browse{margin:24px 0 30px}.browse label{display:block;font-weight:700;margin-bottom:8px}.browse input{width:min(100%,430px);border:1px solid #8b9a8b;border-radius:8px;background:#fff;padding:12px 14px;font:inherit}.browse input:focus-visible,.filters button:focus-visible,.action:focus-visible{outline:3px solid #7c9d43;outline-offset:3px}.filters{display:flex;gap:9px;flex-wrap:wrap;margin-top:18px}.filters button,.action{border:1px solid #9ba99a;background:#fff;color:var(--green);border-radius:6px;padding:9px 15px;font:600 14px 'DM Sans',Arial,sans-serif;cursor:pointer;text-decoration:none}.filters button.active,.filters button:hover,.action:hover{background:var(--green);color:#fff}.browse #result-count{color:#536054;font-size:14px;margin:13px 0 0}.card[hidden],#no-results[hidden]{display:none}.recipe-actions{display:flex;gap:12px;flex-wrap:wrap;margin:24px 0}.recipe-actions .action{display:inline-flex;align-items:center}.article #recipe{scroll-margin-top:24px}@media print{header,footer,.back,.recipe-actions,.recipe-banner{display:none!important}.article{max-width:none;padding:0}.article h1{font-size:30px}.article li{padding:2px 0}.note{margin-top:20px}body{background:white}}
""")

# Prominent recipe-finder panel; keep its input and filters in the same surface.
(p/'style.css').write_text((p/'style.css').read_text()+'''
.browse{position:relative;isolation:isolate;overflow:hidden;margin:32px 0 34px;padding:30px 34px 27px;border-radius:16px;background:linear-gradient(115deg,#203f32 0%,#315945 58%,#476a4b 100%);box-shadow:0 14px 32px rgba(30,58,39,.16);color:#fff}
.browse::before{content:"";position:absolute;z-index:-1;right:-120px;top:-180px;width:410px;height:410px;border-radius:50%;background:radial-gradient(circle,rgba(206,226,151,.19),transparent 67%);pointer-events:none}
.browse label{display:block;margin:0 0 11px;font:600 27px/1.2 'Playfair Display',Georgia,serif;color:#fff}
.browse input{display:block;width:100%;max-width:none;min-height:58px;border:2px solid transparent;border-radius:9px;background:#fff;padding:13px 18px;font:500 17px/1.4 'DM Sans',Arial,sans-serif;color:#203227;box-shadow:0 3px 12px rgba(0,0,0,.1)}
.browse input::placeholder{color:#617266;opacity:1}
.browse input:focus-visible{outline:3px solid #d7eb9b;outline-offset:3px}
.browse .filters{margin:20px 0 0;gap:9px}
.browse .filters button{border:1px solid rgba(255,255,255,.53);border-radius:999px;background:rgba(255,255,255,.09);color:#fff;padding:9px 17px;transition:background .2s,color .2s,border-color .2s}
.browse .filters button.active,.browse .filters button:hover{border-color:#e3edc6;background:#e3edc6;color:#203f32}
.browse #result-count{color:#e0e9db;margin:17px 0 0}
@media(max-width:640px){.browse{padding:24px 20px;margin:24px 0 28px}.browse label{font-size:24px}.browse input{min-height:54px;font-size:16px}.browse .filters{gap:8px}.browse .filters button{padding:8px 13px}}
''')

# Recipe-specific help that answers common preparation and substitution questions.
recipe_help = {
 'lemon-chickpea-rice-bowls': [
  ('Use what you have','Brown rice, couscous or quinoa can replace white rice. Follow the cooking directions for the grain you choose.'),
  ('Keep the vegetables crisp','Dry the chickpeas after rinsing and dice the cucumber just before serving. For packed lunches, store the dressed chickpeas apart from the cucumber.'),
  ('Make it ahead','Cook the rice and mix the dressing the day before. Chill promptly and keep refrigerated; assemble the bowls when ready to eat.')],
 'tomato-white-bean-skillet': [
  ('Choose the beans','Cannellini beans are soft and creamy, but butter beans or navy beans also work. Rinse canned beans to remove excess brine.'),
  ('Adjust the sauce','Simmer uncovered to reduce a thin sauce. If it becomes too thick before serving, stir in a little water.'),
  ('Swap the greens','Chopped kale can replace spinach; add it a few minutes earlier so it has time to soften.')],
 'apple-cinnamon-baked-oats': [
  ('Pick the right oats','Use old-fashioned rolled oats for a tender, defined texture. Instant oats turn soft and steel-cut oats need a different liquid ratio and cook time.'),
  ('Change the fruit','Firm pears can stand in for the apples. If using frozen berries, add them still frozen and allow a few extra minutes in the oven.'),
  ('Check doneness','The center should no longer look liquid. Resting the pan for 10 minutes helps the slices hold together.')],
 'crispy-sheet-pan-potatoes': [
  ('Give them room','If the potatoes are crowded, split them between two pans. A single layer helps the cut sides brown instead of steam.'),
  ('Keep the pieces even','Aim for pieces of similar size so smaller pieces do not burn while larger ones are still firm.'),
  ('Add garlic last','Fresh garlic can scorch at high heat, so toss it with the hot potatoes after roasting.')],
 'creamy-lemon-orzo': [
  ('Stir as it cooks','Orzo can stick to the bottom of the pan. Stir frequently and keep the simmer gentle.'),
  ('Add lemon at the end','Stirring in the juice after cooking keeps its flavor bright. Add a little at a time and taste.'),
  ('Make it without cheese','Omit Parmesan and finish with a spoonful of olive oil. Taste for salt because Parmesan normally supplies some.')],
 'banana-oat-pancakes': [
  ('Let the batter rest','Five minutes gives the ground oats time to absorb the liquid. Add a splash of milk if the batter becomes too thick to spoon.'),
  ('Watch the heat','Keep the skillet at medium-low. Banana makes the batter brown quickly, even before the middle is cooked.'),
  ('Freeze extras','Cool completely, separate with parchment and freeze in a covered container. Reheat until hot throughout.')],
 'honey-yogurt-berry-cups': [
  ('Dry the berries','Water on the berries thins the yogurt and softens the oats. Pat them dry after washing.'),
  ('Keep the crunch','Store toasted oats separately until serving. Their texture changes quickly when layered with yogurt.'),
  ('Try another topping','Chopped pistachios or pumpkin seeds can replace almonds. Check for nut allergies before serving.')],
 'roasted-carrot-tahini-salad': [
  ('Cut evenly','Thin carrot pieces brown faster than thick ones. Cut larger carrots in quarters and small carrots in halves.'),
  ('Fix thick dressing','Tahini sometimes seizes when lemon juice is added. Whisk in water gradually until smooth and pourable.'),
  ('Serve warm or cool','The carrots can be roasted ahead. Keep the dressing separate and spoon it over just before serving.')]
}
for index, recipe in enumerate(recipes):
 slug=recipe['slug'];target=p/'recipes'/slug/'index.html';markup=target.read_text()
 points=''.join('<li><strong>'+escape(heading)+'.</strong> '+escape(detail)+'</li>' for heading,detail in recipe_help[slug])
 next_recipe=recipes[(index+1)%len(recipes)]
 extra='<section class="recipe-guidance"><h2>Helpful cooking notes</h2><ul>'+points+'</ul></section><p class="next-recipe">Cook next: <a href="/recipes/'+next_recipe['slug']+'/">'+escape(next_recipe['title'])+' →</a></p>'
 markup=markup.replace('</article>',extra+'</article>')
 target.write_text(markup)
(p/'style.css').write_text((p/'style.css').read_text()+'''
.recipe-guidance{margin-top:46px;padding-top:3px;border-top:1px solid var(--line)}.recipe-guidance ul{padding-left:22px}.recipe-guidance li{margin:8px 0}.next-recipe{margin-top:40px;padding-top:20px;border-top:1px solid var(--line);font-weight:700}.next-recipe a{color:var(--green)}
''')

# Comfortable reading and touch controls at phone and tablet widths.
(p/'style.css').write_text((p/'style.css').read_text()+'''
html{overflow-x:hidden}body{min-width:0;overflow-wrap:break-word}
.grid{grid-template-columns:repeat(2,minmax(0,1fr))}.card,.card-content,.article,.page{min-width:0}
.brand{flex-shrink:0}nav a{display:inline-flex;align-items:center;min-height:44px}
.filters button,.recipe-actions .action{min-height:44px;display:inline-flex;align-items:center;justify-content:center}
.article img,.page img{max-width:100%;height:auto}
@media(max-width:900px){
 header .wrap{gap:12px;padding-top:14px;padding-bottom:14px}
 nav{gap:8px 16px}
 .hero{padding:58px 0 62px}
 .section{padding:48px 0}
 .grid{gap:18px}
 .card-content{padding:20px}
 .card h3{font-size:26px}
 .art{height:200px}
}
@media(max-width:700px){
 header .wrap{align-items:stretch;flex-direction:column;gap:8px}
 nav{gap:4px 20px}
 .grid{grid-template-columns:1fr;max-width:580px;margin-inline:auto}
 .art{height:clamp(190px,52vw,270px)}
 .hero{padding:48px 0 52px}
 .hero h1{font-size:clamp(38px,9vw,58px)}
 .section{padding:42px 0}
 .browse{margin:25px 0 30px;padding:25px}
 .article,.page{padding-top:42px;padding-bottom:65px}
}
@media(max-width:480px){
 .wrap{padding-left:18px;padding-right:18px}
 header .wrap{padding-top:12px;padding-bottom:10px}
 .brand{font-size:23px}
 nav{justify-content:space-between;gap:4px}
 nav a{font-size:14px;padding:0 3px}
 .hero{padding:40px 0 44px}
 .hero h1{font-size:clamp(36px,10vw,46px);line-height:1.13}
 .hero p{font-size:16px;line-height:1.55}
 .section h2,.article h1,.page h1{font-size:clamp(33px,9vw,42px)}
 .section{padding:36px 0}
 .browse{padding:22px 18px;margin:22px 0 26px;border-radius:13px}
 .browse label{font-size:23px}
 .browse input{font-size:16px;min-height:54px;padding:12px 14px}
 .browse .filters{gap:8px;margin-top:16px}
 .browse .filters button{min-height:44px;padding:9px 14px}
 .card-content{padding:20px}
 .card h3{font-size:27px}
 .recipe-facts{gap:8px 20px}
 .recipe-actions{gap:9px}
 .recipe-actions .action{flex:1 1 145px;text-align:center}
 .article,.page{padding-left:18px;padding-right:18px}
 .article .lead,.page .lead{font-size:18px}
 footer .wrap{gap:18px}
 footer .wrap>div:last-child{display:flex;flex-wrap:wrap;gap:4px 14px}
 footer a{display:inline-flex;align-items:center;min-height:44px;margin-right:0}
}
@media(max-width:350px){.wrap,.article,.page{padding-left:15px;padding-right:15px}.browse{padding:18px 15px}.brand{font-size:21px}}
.section.wrap{padding-left:24px;padding-right:24px}
@media(max-width:480px){.section.wrap{padding-left:18px;padding-right:18px}}
@media(max-width:350px){.section.wrap{padding-left:15px;padding-right:15px}}
.brand{display:inline-flex;align-items:center;gap:11px;min-height:44px;white-space:nowrap}
.brand img{display:block;flex:none;width:42px;height:42px;border-radius:11px}
@media(max-width:480px){.brand{font-size:21px;gap:9px}.brand img{width:38px;height:38px}}
@media(max-width:350px){.brand{font-size:19px;gap:8px}.brand img{width:36px;height:36px}}
.author-line{margin:20px 0 0;color:#536054;font-size:14px;font-weight:600}
.author-line a{color:var(--green);text-underline-offset:3px}
.author-profile{display:grid;grid-template-columns:minmax(0,250px) minmax(0,1fr);gap:28px;align-items:center;margin:25px 0 36px}
.author-profile img{display:block;width:100%;height:auto;aspect-ratio:1;object-fit:cover;border-radius:16px}
.author-profile .lead{margin:8px 0 12px}.author-profile p:last-child{margin-bottom:0}
@media(max-width:600px){.author-profile{grid-template-columns:1fr;gap:20px}.author-profile img{max-width:280px}}
''')

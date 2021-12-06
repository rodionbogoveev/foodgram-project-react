from django.http import HttpResponse

from recipes.models import IngredientRecipe


def create_txt(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=ingredients.txt'
    user = request.user
    for i in IngredientRecipe.objects.filter(recipe__shopping_cart__user=user):
        print(f'{i.ingredient} - {i.amount}')	
    # Create blank list
	lines = []
	# Loop Thu and output
	for venue in venues:
		lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n')

	#lines = ["This is line 1\n", 
	#"This is line 2\n",
	#"This is line 3\n\n",
	#"John Elder Is Awesome!\n"]

	# Write To TextFile
	response.writelines(lines)
	return response

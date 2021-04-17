from thispersondoesnotexist import get_online_person,save_picture
import asyncio
from pythonlib.findface import search_face
import shutil
import time
from pythonlib.nn import calculate

async def f():
	picture = await get_online_person()  # bytes representation of the image


	await save_picture(picture, "abp.png")



def gen_im():
	asyncio.run(f())

	search_face("abp.png")
	#shutil.copy('images/_faces.png','tmp/'+'intrus'+'_'+str(time.time())+'.png')

for i in range(100):
	r = 0
	count = 0
	while r == 0:	
		gen_im()
		from PIL import Image
		s = Image.open('images/_faces.png')
		r = calculate(s)
		conv =['intrus','loan']
		#print(conv[r])
		count +=1
	#s.show()
	shutil.copy('images/_faces.png','tmp/'+'intrus'+'_'+str(time.time())+'.png')
	print(1/count)

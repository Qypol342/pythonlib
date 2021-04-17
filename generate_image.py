from thispersondoesnotexist import get_online_person,save_picture
#import asyncio
from pythonlib.findface import search_face
import shutil
import time
from pythonlib.nn import calculate
from PIL import Image

async def f():
	picture = await get_online_person()  # bytes representation of the image


	await save_picture(picture, "abp.png")



def gen_im():
	await f()

	search_face("abp.png")
	#shutil.copy('images/_faces.png','tmp/'+'intrus'+'_'+str(time.time())+'.png')
def run_gen_im():
	r = 0
	count = 0
	while r == 0:	
		gen_im()
		
		s = Image.open('images/_faces.png')
		r = calculate(s)
		conv =['intrus','loan']

		count +=1
	#s.show()
	shutil.copy('images/_faces.png','tmp/'+'intrus'+'_'+str(time.time())+'.png')



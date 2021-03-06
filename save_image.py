import os
import requests
from bs4 import BeautifulSoup

# 보안코드
scode = ''
# 본인 SP_LOGIN_SESSION 값
login_cookie = ''	

# 캐릭터 목록
character = [
	'no',
	'01jupiter_01toumaa_2',		# 1
	'01jupiter_02syoutam_3',	# 2
	'01jupiter_03hokutoi_1',	# 3
	'02drasta_01terut_2',		# 4
	'02drasta_02kaorus_1',		# 5
	'02drasta_03tubasak_3',		# 6
	'03alte_01keit_3',			# 7
	'03alte_02reik_1',			# 8
	'04beit_01kyoujit_1',		# 9
	'04beit_02pierre_3',		# 10
	'04beit_03minoriw_2',		# 11
	'05w_01yusukea_3',			# 12
	'05w_02kyosukea_1',			# 13
	'06frame_01hideoa_1',		# 14
	'06frame_02ryuk_2',			# 15
	'06frame_03seijis_3',		# 16
	'07sai_01kirion_1',			# 17
	'07sai_02syomah_3',			# 18
	'07sai_03kuros_3',			# 19
	'08highj_01hayatoa_2',		# 20
	'08highj_02junf_1',			# 21
	'08highj_03natukis_1',		# 22
	'08highj_04harunaw_3',		# 23
	'08highj_05sikii_2',		# 24
	'09godp_01suzakua_2',		# 25
	'09godp_02genbuk_1',		# 26
	'10cafe_01yukihirok_3',		# 27
	'10cafe_02souichiros_1',	# 28
	'10cafe_03asselin_2',		# 29
	'10cafe_04makiou_3',		# 30
	'10cafe_05sakim_2',			# 31
	'11mofu_01naoo_1',			# 32
	'11mofu_02sirot_2',			# 33
	'11mofu_03kanonh_3',		# 34
	'12sem_01michioh_1',		# 35
	'12sem_02ruim_3',			# 36
	'12sem_03jiroy_1',			# 37
	'13kogado_01takerut_2',		# 38
	'13kogado_02michirue_2',	# 39
	'13kogado_03reng_2',		# 40
	'14flags_01ryoa_3',			# 41
	'14flags_02daigok_2',		# 42
	'14flags_03kazukit_1',		# 43
	'15legend_01amehikok_1',	# 44
	'15legend_02sorak_3',		# 45
	'15legend_03chrisk_1'		# 46
]

user_agent = 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'
headers = {'User-Agent': user_agent}
dummy_cookies = {'SP_LOGIN_SESSION' : login_cookie}

def setDirPath(dir_path):
	if os.path.isdir(dir_path) == False:
		os.mkdir(dir_path)

def saveImage(dir_path, kind, rare, i, j, P, extension):
	img_url = f'http://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2021081301%2Fcard%2F{kind}%2F{character[i]}_{rare}{j}{P}{scode}.{extension}'
	img_req = requests.get(img_url, cookies=dummy_cookies, headers=headers, stream=True)
	if kind == 'bromide/l':
		img_name = dir_path + f'/{character[i]}_SRBR{j}{P}.{extension}'
	elif kind == 'l' :
		temp = character[i].split('_')[1]
		chara_name = temp[2:len(temp) - 1]
		img_name = dir_path + f'/{chara_name}{rare}{j}{P}.{extension}'
	else :
		chara_name = character[i].split('_', 1)
		img_name = dir_path + f'/{chara_name[1]}_{rare}{j}{P}.{extension}'
	with open(img_name, 'wb') as f:
		f.write(img_req.content)

def saveAllImage(rare, i, j):
	setDirPath('standing')
	saveImage('standing', 'quest', rare, i, j, '', 'png')
	saveImage('standing', 'quest', rare, i, j, 'P', 'png')
	setDirPath('frameCard')
	saveImage('frameCard', 'l', rare, i, j, '', 'jpg')
	saveImage('frameCard', 'l', rare, i, j, 'P', 'jpg')
	if rare == 'SR':
		setDirPath('bromide')
		saveImage('bromide', 'bromide/l', rare, i, j, '', 'jpg')
		saveImage('bromide', 'bromide/l', rare, i, j, 'P', 'jpg')

def isImage(rare, i, j, P):
	img_url = f'http://g12017647.sp.pf.mbga.jp/?url=http%3A%2F%2Fm.i-sidem.idolmaster.jp%2Fimg_sp%2F2021081301%2Fcard%2Fquest%2F{character[i]}_{rare}{j}{P}{scode}.png'
	img_req = requests.get(img_url, cookies=dummy_cookies, headers=headers, stream=True)
	soup = BeautifulSoup(img_req.content, 'html.parser')
	target = soup.find('p')
	if target is None :
		return (True)
	return (False)

def checkCard(i, j):
	after = isImage('SR', i, j, 'P')
	if after == True :
		before = isImage('SR', i, j, '')
		if before == False:
			setDirPath('standing')
			saveImage('standing', 'quest', 'SR', i, j, 'P', 'png')
			setDirPath('frameCard')
			saveImage('frameCard', 'l', 'SR', i, j, 'P', 'jpg')
			setDirPath('bromide')
			saveImage('bromide', 'bromide/l', 'SR', i, j, 'P', 'jpg')
		else:
			saveAllImage('SR', i, j)

def findSRImage():
	# 쥬피터 ~ 코가도
	for i in range(1, 42) :
		for j in range(25, 40) : #SR번호 25~39(40 미포함)까지 이미지 있는지 확인
			checkCard(i, j)

	# 깃발 ~ 레제
	for i in range(42, 47) :
		for j in range(17, 40) : #SR번호 25~39(40 미포함)까지 이미지 있는지 확인
			checkCard(i, j)

def findRImage():
	# 쥬피터 ~ 레제
	for i in range(1, 47) :
		for j in range(17, 40) : #R번호 17~39(40 미포함)까지 이미지 있는지 확인
			find = isImage('R', i, j, 'P')
			if find == True:
				saveAllImage('R', i, j)

with requests.Session() as s:
	try:
		print("Start downloading SR image...")
		findSRImage()
		print("All SR images are downloaded.")
		print("-----------------------------------------------------------------------------------")
		print("Start downloading R image...")
		findRImage()
		print("All R images are downloaded.")
		print("-----------------------------------------------------------------------------------")
		print("Finish.")

	except:
		print('Image Download Error.............')
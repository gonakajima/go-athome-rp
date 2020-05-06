from django.db import models
from django.utils import timezone

class Friend(models.Model):
    jobs = [
                 (1, 'ケアマネ'), \
                 (2, '病院SW'),(3, '病院看護師'),(4, '病院医師'), \
                 (5, 'クリニックSW'),(6, 'クリニック看護師'),(7, 'クリニック医師'), \
                 (8, '訪問介護士'),(9, '施設介護士'), \
                 (10, '患者さん'),(11, '患者さんご家族'),
                 ]

    address = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200, null=True)
    job = models.IntegerField(choices=jobs)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.address + '(' + str(self.job) + ')' + \
            self.mail + '>'

class Distance(models.Model):
    start_id = models.ForeignKey(Friend, on_delete=models.CASCADE)
    target_id = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def __str__(self):
        return '<' + str(self.start_id) + ' puts distance from ' + str(self.target_id) + \
            'as' + '(' + str(self.x) + ',' + str(self.y) + ').>'

class ServiceAttr(models.Model):
    attributes = models.CharField(max_length=10)
    
    def __str__(self):
        return str(self.attributes)
            
class Service(models.Model):
    attributes = [
                 (1, '在宅クリニック'),(2, '居宅介護支援'),(3, '訪問看護ST'),(4, '急性期病院'), \
                 (5, '緩和ケア病棟'),(6, '在宅療養支援病院'),(7, '外来クリニック'),(8, '歯科クリニック'), \
                 (9, 'グループホーム'),(10, '介護付有料'),(11, '住宅型有料'),(12, 'サ高住'), \
                 (13, '小規模多機能'),(14, '特養'),(15, '老健'),(16, '他の施設'), \
                 (17, '訪問介護'),(18, '訪問入浴'),(19, '定期巡回'),(20, 'デイサービス'),(21, 'ショートステイ'),
                 ]
    name = models.CharField(max_length=100, null=True)
    attribute = models.IntegerField(choices=attributes)
    address = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200, null=True)
    phone = models.IntegerField()
    attr = models.ManyToManyField(ServiceAttr)
    
    def __str__(self):
        return str(self.name)
'''
    phone_regex = RegexValidator(
            regex=r(
            (\d{1,4}|\(\d{1,4}\))
            (\s|-)
            (\d{1,4})
            (\s|-)
            (\d{3,4})
            ), re.VERBOSE, message="「011-802-7823」の形式でお願いします")
    phone = models.IntegerField(validators=[phone_regex], max_length=12, blank=True)
'''

class ServicePost(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    #photo = models.ImageField(upload_to='image/')
    name = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.title)
    
class PatientNeed(models.Model):
    status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.status)

class Patient(models.Model):
    REFERRER_CHOICES = [(1, 'ケアマネ'),(2, '病院SW'),(3, '訪問看護師'),(4, '病院看護師'),(5, 'ご家族')]
    GENDER_CHOICES = [(1, '女性'),(2, '男性')]
    PURPOSE_CHOICES = [
        (1, '医療的介護'),(2, '身体介護'),(3, '認知症介護'),(4, '生活介護'),(5, 'ターミナルケア'),(6, '新型コロナ感染疑い')
    ]
    
    referrer_name = models.CharField(verbose_name='ご依頼者',default='',help_text='あなた様のお名前',max_length=30)
    attribute = models.IntegerField(verbose_name='ご関係',choices=REFERRER_CHOICES,help_text='患者様とのご関係',default=5)
    phone = models.IntegerField(verbose_name='電話番号',help_text='連絡のとれる電話番号',default='')
    patient_name = models.CharField(verbose_name='患者様',default='',help_text='患者様のお名前',max_length=30)
    birthday = models.DateField(verbose_name='生年月日',help_text='患者様の生年月日 例：「1977-10-30」',default='')
    gender = models.IntegerField(verbose_name='性別',choices=GENDER_CHOICES,default=1)
    purpose = models.IntegerField(verbose_name='ご病状',help_text='一つを選択',choices=PURPOSE_CHOICES,default=6)
    address = models.CharField(verbose_name='住所',default='',help_text='例:「札幌市中央区南1条東2丁目8-1」',max_length=100)
    comment = models.TextField('コメント',default='',help_text='必要あればなんでもご記載ください。',max_length=500, blank=True)
    file = models.ImageField(upload_to='media/', default='',verbose_name='保険証・薬情報',blank=True)
    need = models.ManyToManyField(PatientNeed)
    
    def __str__(self):
        return str(self.referrer_name) + ':' + str(self.phone) + ':' + str(self.address)
            
    
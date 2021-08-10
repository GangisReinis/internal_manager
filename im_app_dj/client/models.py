from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class attr_company(models.Model):
    company_name      = models.CharField(max_length=255, unique=True, help_text='Enter company full name')
    slug              = models.SlugField()
    registration_no   = models.CharField(max_length=20, unique=True, help_text='Enter company registration number')
    main_address      = models.CharField(max_length=250, help_text='Enter company registration address')
    post_address      = models.CharField(max_length=250, null=True, blank=True, help_text='Enter company postal address')
    bank_iban         = models.CharField(max_length=100, null=True, blank=True, help_text='Enter company Bank IBAN number')
    keyword           = models.CharField(max_length=50, null=True, blank=True, unique=True, help_text='Enter company Tildes JUMIS keyword')
    comp_date         = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    vat_date          = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    mun_period_from   = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    mun_period_to     = models.DateField(auto_now=False, null=True, blank=True, auto_now_add=False)
    nace_code         = models.CharField(max_length=20, null=True, blank=True, help_text='Enter company NACE code')
    nace_desc         = models.CharField(max_length=100, null=True, blank=True, help_text='Enter company NACE description')
    contr_id          = models.CharField(max_length=30, null=True, blank=True, help_text='Enter sales contract id if exists')
    is_not_active     = models.BooleanField(default=False)
    comp_form         = models.CharField(max_length=100, null=True, blank=True, help_text='Enter company status/form')
    risk_asses_1      = models.CharField(max_length=250, null=True, blank=True, help_text='2. Darījumu raksturs')
    risk_asses_2      = models.CharField(max_length=250, null=True, blank=True, help_text='3. Personīga tikšanās')
    risk_asses_3      = models.CharField(max_length=250, null=True, blank=True, help_text='4. Politiski nozīmīga persona')
    risk_asses_4      = models.CharField(max_length=250, null=True, blank=True, help_text='5. Vai PLG ir iekļauts sankciju sarakstos?')
    risk_asses_5      = models.CharField(max_length=250, null=True, blank=True, help_text='6. PLG rezidences valsts')
    risk_asses_6      = models.CharField(max_length=250, null=True, blank=True, help_text='7. Klienta saimnieciskās darbības ilgums')
    risk_asses_7      = models.CharField(max_length=250, null=True, blank=True, help_text='8. Cik ilgi pazīstams PLG')
    risk_asses_8      = models.CharField(max_length=250, null=True, blank=True, help_text='9. Saimnieciskās darbības risks')
    risk_asses_9      = models.CharField(max_length=250, null=True, blank=True, help_text='10. Kādās valstīs notiek pakalpojumu sniegšana')
    risk_asses_10     = models.CharField(max_length=250, null=True, blank=True, help_text='11. Informācija par amatpersonām masu medijos')
    risk_asses_11     = models.CharField(max_length=50, null=True, blank=True, help_text='NILLTFN riska novērtējums')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.company_name)
        super(attr_company, self).save(*args, **kwargs)

    def __str__(self):
        return self.company_name

    class Meta:
        ordering = ['company_name']

    def get_absolute_url(self):
        """Returns the url to access a particular client instance."""
        return reverse('client-detail', kwargs={'slug':str(self.slug)})

class attr_employee(models.Model):
    employee     = models.CharField(max_length=100, help_text='Enter employee full name')
    role         = models.CharField(max_length=100, null=True, blank=True, help_text='Enter employee role')
    email        = models.EmailField(max_length=254, null=True, blank=True, help_text='Enter email')
    tele         = models.CharField(max_length=100, null=True, blank=True, help_text='Enter employee telephone number')
    is_board     = models.BooleanField(default=False)
    is_sh_holder = models.BooleanField(default=False)
    is_main_benf = models.BooleanField(default=False)
    company      = models.ForeignKey(attr_company,db_column='slug',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.employee}'

    class Meta:
        ordering = ['employee']
        
    def get_absolute_url(self):
        """Returns the url to access a particular employee instance."""
        return reverse('employee-detail', kwargs={'slug' : str(self.company.slug),'pk' : int(self.pk)})

class attr_asset(models.Model):
    """Model representing a Company assets."""
    asset_type     = models.CharField(max_length=50, help_text='Enter asset type (e.g car, pc, telephone)')
    asset_id       = models.CharField(max_length=50, help_text='Enter asset ID (e.g LV-1009)')
    asset_contr_id = models.CharField(max_length=50, null=True, blank=True, help_text='Enter contract id for asset')
    asset_desc     = models.CharField(max_length=250, null=True, blank=True, help_text='Enter short description about asset')
    company        = models.ForeignKey(attr_company, db_column='slug', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        ordering = ['asset_type']

    def get_absolute_url(self):
        """Returns the url to access a particular asset instance."""
        return reverse('asset-detail', kwargs={'slug' : str(self.company.slug),'pk' : int(self.pk)})

class attr_related(models.Model):
    """Model representing a related companies for Company (client)."""
    rel_comp_name = models.CharField(max_length=100, help_text='Enter related company name')
    rel_comp_reg  = models.CharField(max_length=20, null=True, blank=True, unique=True, help_text='Enter company registration number')
    description   = models.CharField(max_length=250, default="no description available.", help_text='Enter related company name')
    company       = models.ForeignKey(attr_company,db_column='slug',on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.rel_comp_name}'

    class Meta:
        ordering = ['rel_comp_name']

    def get_absolute_url(self):
        """Returns the url to access a particular related company instance."""
        return reverse('related-detail', kwargs={'slug' : str(self.company.slug),'pk' : int(self.pk)})

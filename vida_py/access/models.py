from datetime import datetime

from sqlalchemy import BINARY, Boolean, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class ASConfig(Model):
    __bind_key__ = "access"
    __tablename__ = "ASConfig"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    ASConfigType: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class ASInstance(Model):
    __bind_key__ = "access"
    __tablename__ = "ASInstance"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkComputerInfo: Mapped[str] = mapped_column(ForeignKey("ComputerInfo.Id"))
    SyncId: Mapped[str] = mapped_column(String)
    PIEClientId: Mapped[int] = mapped_column(Integer)
    fkASConfig: Mapped[str] = mapped_column(ForeignKey("ASConfig.Id"))
    fkCustomerOrg: Mapped[str] = mapped_column(ForeignKey("CustomerOrgs.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class AdminRules(Model):
    __bind_key__ = "access"
    __tablename__ = "AdminRules"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    RuleCode: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class ApplicationProperty(Model):
    __bind_key__ = "access"
    __tablename__ = "ApplicationProperty"

    key: Mapped[str] = mapped_column(String(150), primary_key=True)
    value: Mapped[str] = mapped_column(String(150))


class ClientLog(Model):
    __bind_key__ = "access"
    __tablename__ = "ClientLog"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    LogEntry: Mapped[str] = mapped_column(String(1073741823))
    SentToVoccs: Mapped[bool] = mapped_column(Boolean)
    CreationDate: Mapped[datetime] = mapped_column(DateTime)
    EventType: Mapped[str] = mapped_column(String(50))


class ComputerInfo(Model):
    __bind_key__ = "access"
    __tablename__ = "ComputerInfo"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    ComputerName: Mapped[str] = mapped_column(String(50))
    MacAddress: Mapped[str] = mapped_column(String(250))
    MotherBoardId: Mapped[str] = mapped_column(String(40))


class Countries(Model):
    __bind_key__ = "access"
    __tablename__ = "Countries"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    CountryCode: Mapped[str] = mapped_column(String(50))
    distrEmail: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class Country_DeliveryTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "Country_DeliveryTypes"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCountry: Mapped[str] = mapped_column(ForeignKey("Countries.Id"))
    fkCustomerType: Mapped[str] = mapped_column(ForeignKey("CustomerTypes.Id"))
    fkDeliveryType: Mapped[str] = mapped_column(ForeignKey("DeliveryTypes.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class CustomerOrgs(Model):
    __bind_key__ = "access"
    __tablename__ = "CustomerOrgs"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Created: Mapped[datetime] = mapped_column(DateTime)
    ContactName: Mapped[str] = mapped_column(String(50))
    ContactEmail: Mapped[str] = mapped_column(String(100))
    PhoneNo: Mapped[str] = mapped_column(String(50))
    FaxNo: Mapped[str] = mapped_column(String(50))
    Address1: Mapped[str] = mapped_column(String(50))
    Address2: Mapped[str] = mapped_column(String(50))
    Address3: Mapped[str] = mapped_column(String(50))
    City: Mapped[str] = mapped_column(String(50))
    ZipCode: Mapped[str] = mapped_column(String(50))
    US_State: Mapped[str] = mapped_column(String(20))
    CompanyName: Mapped[str] = mapped_column(String(50))
    DMSUrl: Mapped[str] = mapped_column(String(100))
    DMSurlCAS: Mapped[str] = mapped_column(String(100))
    QW90Id: Mapped[str] = mapped_column(String(50))
    ParmaId: Mapped[str] = mapped_column(String(50))
    PartnerId: Mapped[str] = mapped_column(String(50))
    District: Mapped[str] = mapped_column(String(50))
    Customer: Mapped[str] = mapped_column(String(50))
    WSLSiteId: Mapped[str] = mapped_column(String(50))
    Suspended: Mapped[bool] = mapped_column(Boolean)
    IsDMSavailableOnCAS: Mapped[bool] = mapped_column(Boolean)
    UseProxyForDMSOnAIOC: Mapped[bool] = mapped_column(Boolean)
    NotAllowedToBuySubscriptions: Mapped[bool] = mapped_column(Boolean)
    FetchPriceFromMP: Mapped[bool] = mapped_column(Boolean)
    ShowIndependentOrderButton: Mapped[bool] = mapped_column(Boolean)
    fkPartnerGroup: Mapped[str] = mapped_column(ForeignKey("PartnerGroups.Id"))
    fkLanguage: Mapped[str] = mapped_column(ForeignKey("Languages.Id"))
    fkCountries: Mapped[str] = mapped_column(ForeignKey("Countries.Id"))
    fkDeliveryType: Mapped[str] = mapped_column(ForeignKey("DeliveryTypes.Id"))
    fkDistributionType: Mapped[str] = mapped_column(ForeignKey("DistributionTypes.Id"))
    fkCustomerType: Mapped[str] = mapped_column(ForeignKey("CustomerTypes.Id"))
    fkOrgParent: Mapped[str] = mapped_column(ForeignKey("CustomerOrgs.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    AutomaticPartDetailsEnabled: Mapped[bool] = mapped_column(Boolean)
    fkMpCountries: Mapped[str] = mapped_column(ForeignKey("Countries.Id"))


class CustomerTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "CustomerTypes"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Type: Mapped[str] = mapped_column(String(50))
    PartnerPfx: Mapped[int] = mapped_column(Integer)
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class DeliveryTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "DeliveryTypes"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Type: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class DistributionTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "DistributionTypes"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Type: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class GpssPartNumberTranslation(Model):
    __bind_key__ = "access"
    __tablename__ = "GpssPartNumberTranslation"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCustomerOrg: Mapped[str] = mapped_column(ForeignKey("CustomerOrgs.Id"))
    actualPartNumber: Mapped[str] = mapped_column(String(15))
    fictivePartNumber: Mapped[str] = mapped_column(String(15))
    Description: Mapped[str] = mapped_column(String(100))
    objVersion: Mapped[int] = mapped_column(Integer)
    changed: Mapped[datetime] = mapped_column(DateTime)
    price: Mapped[float] = mapped_column(Numeric, default=(0))


class InstalledLanguage(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledLanguage"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkInstalledPublication: Mapped[str] = mapped_column(
        ForeignKey("InstalledPublication.Id")
    )
    fkLanguage: Mapped[str] = mapped_column(ForeignKey("Languages.Id"))
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class InstalledPublication(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledPublication"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    PublicationTitle: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class InstalledUpdate(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledUpdate"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkInstalledPublication: Mapped[str] = mapped_column(
        ForeignKey("InstalledPublication.Id")
    )
    InstallDate: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    UpdateTitle: Mapped[str] = mapped_column(String(50))


class Languages(Model):
    __bind_key__ = "access"
    __tablename__ = "Languages"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    LanguageCode: Mapped[str] = mapped_column(String(50))
    Cid: Mapped[int] = mapped_column(Integer)
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class LexiconId_Descriptions(Model):
    __bind_key__ = "access"
    __tablename__ = "LexiconId_Descriptions"

    fkLexiconId: Mapped[str] = mapped_column(
        String, primary_key=ForeignKey("LexiconIds.Id")
    )
    fkLanguage: Mapped[str] = mapped_column(
        String, primary_key=ForeignKey("Languages.Id")
    )
    Description: Mapped[str] = mapped_column(String(255))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class LexiconIds(Model):
    __bind_key__ = "access"
    __tablename__ = "LexiconIds"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    SourceEntity: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class MenuPricingCustomerOrgLabourRate(Model):
    __bind_key__ = "access"
    __tablename__ = "MenuPricingCustomerOrgLabourRate"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCustomerOrg: Mapped[str] = mapped_column(ForeignKey("CustomerOrgs.Id"))
    price: Mapped[float] = mapped_column(Numeric)
    objVersion: Mapped[int] = mapped_column(Integer)
    Changed: Mapped[datetime] = mapped_column(DateTime)


class MenuPricing_MarketFactor(Model):
    __bind_key__ = "access"
    __tablename__ = "MenuPricing_MarketFactor"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCountries: Mapped[str] = mapped_column(ForeignKey("Countries.Id"))
    factor: Mapped[int] = mapped_column(Integer)
    objVersion: Mapped[int] = mapped_column(Integer)
    changed: Mapped[datetime] = mapped_column(DateTime)


class PartnerGroups(Model):
    __bind_key__ = "access"
    __tablename__ = "PartnerGroups"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    PartnerGroupCode: Mapped[str] = mapped_column(String(10))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class PublicationLanguage(Model):
    __bind_key__ = "access"
    __tablename__ = "PublicationLanguage"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkPublication: Mapped[str] = mapped_column(ForeignKey("Publications.Id"))
    fkLanguage: Mapped[str] = mapped_column(ForeignKey("Languages.Id"))
    PublishDate: Mapped[datetime] = mapped_column(DateTime)
    PublicationSize: Mapped[int] = mapped_column(Integer)
    PublicationFilename: Mapped[str] = mapped_column(String(100))
    Info: Mapped[str] = mapped_column(String(100))
    Severity: Mapped[str] = mapped_column(String(50))
    Status: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    CheckSum: Mapped[str] = mapped_column(String(50))


class PublicationTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "PublicationTypes"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    Type: Mapped[str] = mapped_column(String(10))
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class Publications(Model):
    __bind_key__ = "access"
    __tablename__ = "Publications"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkPublicationType: Mapped[str] = mapped_column(ForeignKey("PublicationTypes.Id"))
    PublicationTitle: Mapped[str] = mapped_column(String(50))
    Info: Mapped[str] = mapped_column(String(200))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    ParentPublicationTitle: Mapped[str] = mapped_column(String(50))


class RecentSymptoms(Model):
    __bind_key__ = "access"
    __tablename__ = "RecentSymptoms"

    fkRecentVins: Mapped[str] = mapped_column(
        String, ForeignKey("RecentVINs.Id"), primary_key=True
    )
    SymptomId: Mapped[int] = mapped_column(Integer, primary_key=True)
    CscSymptom: Mapped[str] = mapped_column(String(2))
    JobNo: Mapped[str] = mapped_column(String(10))


class RecentVINs(Model):
    __bind_key__ = "access"
    __tablename__ = "RecentVINs"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    VIN: Mapped[str] = mapped_column(String(20))
    fkUser: Mapped[str] = mapped_column(ForeignKey("Users.Id"))
    fkRecentVinOverridden: Mapped[str] = mapped_column(
        ForeignKey("RecentVinOverridden.Id")
    )
    chassisNumber: Mapped[str] = mapped_column(String(10))
    registrationNumber: Mapped[str] = mapped_column(String(20))
    fkPartnerGroup: Mapped[int] = mapped_column(ForeignKey("PartnerGroups.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class RecentVinOverridden(Model):
    __bind_key__ = "access"
    __tablename__ = "RecentVinOverridden"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkVehicleModel: Mapped[int] = mapped_column(ForeignKey("VehicleModel.Id"))
    fkModelYear: Mapped[int] = mapped_column(ForeignKey("ModelYear.Id"))
    fkEngine: Mapped[int] = mapped_column(ForeignKey("Engine.Id"))
    fkTransmission: Mapped[int] = mapped_column(ForeignKey("Transmission.Id"))


class ServerConfig(Model):
    __bind_key__ = "access"
    __tablename__ = "ServerConfig"

    id: Mapped[str] = mapped_column(String, primary_key=True)
    InboxPath: Mapped[str] = mapped_column(String(255))
    QW90ServiceName: Mapped[str] = mapped_column(String(255))
    DasigServiceName: Mapped[str] = mapped_column(String(255))
    MailTransmitterServiceName: Mapped[str] = mapped_column(String(255))
    SpScriptServiceName: Mapped[str] = mapped_column(String(255))
    SWODLServiceName: Mapped[str] = mapped_column(String(255))
    SystemPollerServiceName: Mapped[str] = mapped_column(String(255))
    TIEServiceName: Mapped[str] = mapped_column(String(255))
    ClientInfoServiceName: Mapped[str] = mapped_column(String(255))
    DROServiceName: Mapped[str] = mapped_column(String(255))
    ProxyServletURL: Mapped[str] = mapped_column(String(255))
    AdministrationURL: Mapped[str] = mapped_column(String(255))
    BaseDataURL: Mapped[str] = mapped_column(String(255))
    PublishAreaURL: Mapped[str] = mapped_column(String(255))
    IntegrationURL: Mapped[str] = mapped_column(String(255))
    IntegrationUserId: Mapped[str] = mapped_column(String(50))
    IntegrationPassword: Mapped[str] = mapped_column(String(50))
    ComPort: Mapped[str] = mapped_column(String(50))
    DmsTimeout: Mapped[int] = mapped_column(Integer)
    SessionTimeOut: Mapped[int] = mapped_column(Integer)
    MaxRecentVin: Mapped[int] = mapped_column(Integer)
    DealerLogotypeFileLocation: Mapped[str] = mapped_column(String(255))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    CentralSystemConnectionType: Mapped[str] = mapped_column(String(8))
    PieServiceName: Mapped[str] = mapped_column(String(255))
    SurveillancServiceName: Mapped[str] = mapped_column(String(255))
    CwlServiceName: Mapped[str] = mapped_column(String(255))
    proxyServiceName: Mapped[str] = mapped_column(String(255))
    SwdlAreaURL: Mapped[str] = mapped_column(String(255))


class ServerConsistency(Model):
    __bind_key__ = "access"
    __tablename__ = "ServerConsistency"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkInstalledPublication: Mapped[str] = mapped_column(
        ForeignKey("InstalledPublication.Id")
    )
    fkInstalledUpdate: Mapped[str] = mapped_column(ForeignKey("InstalledUpdate.Id"))
    ForceSynch: Mapped[bool] = mapped_column(Boolean)
    LastClientLog: Mapped[datetime] = mapped_column(DateTime)
    LastLogin: Mapped[datetime] = mapped_column(DateTime)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    UninstalledUpdateCounter: Mapped[int] = mapped_column(Integer)
    ForceNewInstallation: Mapped[bool] = mapped_column(Boolean)
    difference: Mapped[int] = mapped_column(Integer)


class SessionCache(Model):
    __bind_key__ = "access"
    __tablename__ = "SessionCache"

    UserId: Mapped[str] = mapped_column(String(50), primary_key=True)
    SessionId: Mapped[str] = mapped_column(String(50))


class UserRoles(Model):
    __bind_key__ = "access"
    __tablename__ = "UserRoles"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCustomerType: Mapped[str] = mapped_column(ForeignKey("CustomerTypes.Id"))
    Role: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(ForeignKey("LexiconIds.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class User_DMSSettings(Model):
    __bind_key__ = "access"
    __tablename__ = "User_DMSSettings"

    fkUser: Mapped[str] = mapped_column(ForeignKey("Users.Id"), primary_key=True)
    dmsKey: Mapped[str] = mapped_column(String(50), primary_key=True)
    dmsValue: Mapped[str] = mapped_column(String(50))


class User_PersonalComments(Model):
    __bind_key__ = "access"
    __tablename__ = "User_PersonalComments"

    CommentId: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkUserId: Mapped[str] = mapped_column(ForeignKey("Users.Id"))
    TargetElementId: Mapped[str] = mapped_column(String(50))
    TargetTypeId: Mapped[int] = mapped_column(Integer)
    CommentBody: Mapped[str] = mapped_column(String(500))
    CreationDate: Mapped[datetime] = mapped_column(DateTime)
    ModifiedDate: Mapped[datetime] = mapped_column(DateTime)


class User_Settings(Model):
    __bind_key__ = "access"
    __tablename__ = "User_Settings"

    fkUser: Mapped[str] = mapped_column(String, primary_key=ForeignKey("Users.Id"))
    SettingKey: Mapped[str] = mapped_column(String(50), primary_key=True)
    SettingValue: Mapped[str] = mapped_column(String(50))


class User_ShoppingListParts(Model):
    __bind_key__ = "access"
    __tablename__ = "User_ShoppingListParts"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkShoppingList: Mapped[int] = mapped_column(ForeignKey("User_ShoppingLists.Id"))
    isAddedManually: Mapped[bool] = mapped_column(Boolean, default=0)
    PartNumber: Mapped[str] = mapped_column(String(50))
    SectionCode: Mapped[str] = mapped_column(String(16))
    SelectedVehicleProfile: Mapped[str] = mapped_column(String(255))
    ChassisNumber: Mapped[str] = mapped_column(String(6))
    Vin: Mapped[str] = mapped_column(String(17))
    RegistrationNumber: Mapped[str] = mapped_column(String(20))
    isSoftwareProduct: Mapped[bool] = mapped_column(Boolean, default=0)
    Description: Mapped[str] = mapped_column(String(255))
    Quantity: Mapped[float] = mapped_column(Numeric)
    Price: Mapped[float] = mapped_column(Numeric)
    JobNumber: Mapped[str] = mapped_column(String(10))
    PartsPrefix: Mapped[str] = mapped_column(String(5))
    isAddedToSoftwareManager: Mapped[bool] = mapped_column(Boolean, default=0)
    Changed: Mapped[datetime] = mapped_column(DateTime)


class User_ShoppingLists(Model):
    __bind_key__ = "access"
    __tablename__ = "User_ShoppingLists"

    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkUser: Mapped[str] = mapped_column(ForeignKey("Users.Id"))
    ShoppingListName: Mapped[str] = mapped_column(String(50))
    ShoppingListNumber: Mapped[int] = mapped_column(Integer, default=0)
    Changed: Mapped[datetime] = mapped_column(DateTime)


class Users(Model):
    __bind_key__ = "access"
    __tablename__ = "Users"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    UserId: Mapped[str] = mapped_column(String(50))
    LicenceKey: Mapped[bytes] = mapped_column(BINARY(2147483647))
    FirstName: Mapped[str] = mapped_column(String(50))
    LastName: Mapped[str] = mapped_column(String(50))
    Password: Mapped[str] = mapped_column(String(50))
    IsActive: Mapped[bool] = mapped_column(Boolean)
    IsSuspended: Mapped[bool] = mapped_column(Boolean)
    Email: Mapped[str] = mapped_column(String(50))
    Phone: Mapped[str] = mapped_column(String(50))
    MobilePhone: Mapped[str] = mapped_column(String(50))
    DMSUserId: Mapped[str] = mapped_column(String(50))
    DMSPassword: Mapped[str] = mapped_column(String(50))
    DMSDefaultPrefix: Mapped[str] = mapped_column(String(50))
    DMSURL: Mapped[str] = mapped_column(String(200))
    TIEUserId: Mapped[str] = mapped_column(String(50))
    TIEPassword: Mapped[str] = mapped_column(String(50))
    fkAdminRule: Mapped[str] = mapped_column(ForeignKey("AdminRules.Id"))
    fkCustomerOrg: Mapped[str] = mapped_column(ForeignKey("CustomerOrgs.Id"))
    fkUserRoles: Mapped[str] = mapped_column(ForeignKey("UserRoles.Id"))
    fkLanguage: Mapped[str] = mapped_column(ForeignKey("Languages.Id"))
    fkPartnerGroup: Mapped[str] = mapped_column(ForeignKey("PartnerGroups.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    fkUserPermission: Mapped[str] = mapped_column(String)  # Foreign Key
    IsPriceWithVAT: Mapped[bool] = mapped_column(Boolean, default=1)
    DMSURLVOW: Mapped[str] = mapped_column(String(200))


class VinPartnerGroupCountries(Model):
    __bind_key__ = "access"
    __tablename__ = "VinPartnerGroupCountries"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    fkCountry: Mapped[str] = mapped_column(ForeignKey("Countries.Id"))
    fkVinPartnerGroup: Mapped[str] = mapped_column(ForeignKey("VinPartnerGroups.Id"))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class VinPartnerGroups(Model):
    __bind_key__ = "access"
    __tablename__ = "VinPartnerGroups"

    Id: Mapped[str] = mapped_column(String, primary_key=True)
    VinPartnerGroupCode: Mapped[str] = mapped_column(String(50))
    fkPartnerGroup: Mapped[int] = mapped_column(ForeignKey("PartnerGroups.Id"))
    decodePos9: Mapped[str] = mapped_column(String(1))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class WorkList(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    listTitle: Mapped[str] = mapped_column(String(50))
    orderNumber: Mapped[str] = mapped_column(String(50))
    fkUserIdCreatedBy: Mapped[int] = mapped_column(ForeignKey("Users.Id"))
    listType: Mapped[str] = mapped_column(String(50), default="NONE")
    fkUserIdLockedBy: Mapped[int] = mapped_column(ForeignKey("Users.Id"))
    comment: Mapped[str] = mapped_column(String(-1))
    fkWorkList_Vehicle: Mapped[int] = mapped_column(ForeignKey("WorkList_Vehicle.Id"))
    deleted: Mapped[bool] = mapped_column(Boolean, default=(0))
    version: Mapped[int] = mapped_column(Integer, default=(1))
    partnerId: Mapped[str] = mapped_column(String(50))


class WorkList_Csc(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Csc"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkList: Mapped[int] = mapped_column(ForeignKey("WorkList.Id"))
    csc: Mapped[str] = mapped_column(String(2))
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    qbNumber: Mapped[str] = mapped_column(String(7))
    qbDescription: Mapped[str] = mapped_column(String(20))


class WorkList_CscText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_CscText"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkCsc: Mapped[int] = mapped_column(ForeignKey("WorkList_Csc.Id"))
    isoLanguage: Mapped[str] = mapped_column(String(5))
    componentFunction: Mapped[str] = mapped_column(String(255))
    component: Mapped[str] = mapped_column(String(255))
    deviation: Mapped[str] = mapped_column(String(255))
    comment1: Mapped[str] = mapped_column(String(255))
    comment2: Mapped[str] = mapped_column(String(255))


class WorkList_Operation(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    operationNumber: Mapped[str] = mapped_column(String(5))
    operationType: Mapped[int] = mapped_column(Integer)
    quantity: Mapped[int] = mapped_column(Integer)
    skilllevel: Mapped[str] = mapped_column(String(3))
    variantDescription: Mapped[str] = mapped_column(String(255))
    maxFix: Mapped[str] = mapped_column(String(1))
    jobValue: Mapped[float] = mapped_column(Numeric)
    maxQuantity: Mapped[int] = mapped_column(Integer)
    remedyCode: Mapped[int] = mapped_column(Integer)
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    packageOperationType: Mapped[str] = mapped_column(String(10))
    specification: Mapped[str] = mapped_column(String(20))
    price: Mapped[float] = mapped_column(Numeric)
    qbNumber: Mapped[str] = mapped_column(String(7))
    qbDescription: Mapped[str] = mapped_column(String(20))


class WorkList_OperationText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_OperationText"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkOperationTitle: Mapped[int] = mapped_column(Integer)  # Foreign Key
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(255))


class WorkList_Operation_List(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation_List"

    fkWorkList: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList.Id")
    )
    fkWorkList_Operation: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Operation.Id")
    )


class WorkList_Operation_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation_Package"

    fkWorkList_Package: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Package.Id")
    )
    fkWorkList_Operation: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Operation.Id")
    )


class WorkList_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Package"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkList: Mapped[int] = mapped_column(ForeignKey("WorkList.Id"))
    packageNumber: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column(Integer)
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    usingFixedPrice: Mapped[bool] = mapped_column(Boolean)


class WorkList_PackageText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PackageText"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPackageTitle: Mapped[int] = mapped_column(Integer)  # Foreign Key
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(1000))


class WorkList_Part(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    partNumber: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[float] = mapped_column(Numeric)
    software: Mapped[bool] = mapped_column(Boolean)
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Numeric)
    fkWorkList_Vehicle: Mapped[int] = mapped_column(ForeignKey("WorkList_Vehicle.Id"))


class WorkList_PartText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PartText"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkPartTitle: Mapped[int] = mapped_column(Integer)  # Foreign Key
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(255))


class WorkList_Part_List(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part_List"

    fkWorkList: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList.Id")
    )
    fkWorkList_Part: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Part.Id")
    )


class WorkList_Part_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part_Package"

    fkWorkList_Package: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Package.Id")
    )
    fkWorkList_Part: Mapped[int] = mapped_column(
        Integer, primary_key=ForeignKey("WorkList_Part.Id")
    )


class WorkList_PostponedQb(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PostponedQb"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkList: Mapped[int] = mapped_column(ForeignKey("WorkList.Id"))
    qbNumber: Mapped[str] = mapped_column(String(7))
    qbDescription: Mapped[str] = mapped_column(String(20))


class WorkList_Settings(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fkWorkListUser: Mapped[int] = mapped_column(ForeignKey("WorkList_User.Id"))
    settingName: Mapped[str] = mapped_column(String(50))
    settingValue: Mapped[str] = mapped_column(String(50))


class WorkList_User(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_User"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userId: Mapped[str] = mapped_column(String(50))
    partnerId: Mapped[str] = mapped_column(String(50))
    idSelectedWorkList: Mapped[int] = mapped_column(Integer)


class WorkList_Vehicle(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Vehicle"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    profileId: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    vin: Mapped[str] = mapped_column(String(17))

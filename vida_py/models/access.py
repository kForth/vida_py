from datetime import datetime

from sqlalchemy import BINARY, Boolean, DateTime, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column

from vida_py.models import Model


class ASConfig(Model):
    __bind_key__ = "access"
    __tablename__ = "ASConfig"

    ASConfigType: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class ASInstance(Model):
    __bind_key__ = "access"
    __tablename__ = "ASInstance"

    fkComputerInfo: Mapped[str] = mapped_column(String)
    SyncId: Mapped[str] = mapped_column(String)
    PIEClientId: Mapped[int] = mapped_column(Integer)
    fkASConfig: Mapped[str] = mapped_column(String)
    fkCustomerOrg: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class AdminRules(Model):
    __bind_key__ = "access"
    __tablename__ = "AdminRules"

    RuleCode: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class ApplicationProperty(Model):
    __bind_key__ = "access"
    __tablename__ = "ApplicationProperty"

    value: Mapped[str] = mapped_column(String(150))


class ClientLog(Model):
    __bind_key__ = "access"
    __tablename__ = "ClientLog"

    LogEntry: Mapped[str] = mapped_column(String(1073741823))
    SentToVoccs: Mapped[bool] = mapped_column(Boolean)
    CreationDate: Mapped[datetime] = mapped_column(DateTime)
    EventType: Mapped[str] = mapped_column(String(50))


class ComputerInfo(Model):
    __bind_key__ = "access"
    __tablename__ = "ComputerInfo"

    ComputerName: Mapped[str] = mapped_column(String(50))
    MacAddress: Mapped[str] = mapped_column(String(250))
    MotherBoardId: Mapped[str] = mapped_column(String(40))


class Countries(Model):
    __bind_key__ = "access"
    __tablename__ = "Countries"

    CountryCode: Mapped[str] = mapped_column(String(50))
    distrEmail: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class Country_DeliveryTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "Country_DeliveryTypes"

    fkCountry: Mapped[str] = mapped_column(String)
    fkCustomerType: Mapped[str] = mapped_column(String)
    fkDeliveryType: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class CustomerOrgs(Model):
    __bind_key__ = "access"
    __tablename__ = "CustomerOrgs"

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
    fkPartnerGroup: Mapped[str] = mapped_column(String)
    fkLanguage: Mapped[str] = mapped_column(String)
    fkCountries: Mapped[str] = mapped_column(String)
    fkDeliveryType: Mapped[str] = mapped_column(String)
    fkDistributionType: Mapped[str] = mapped_column(String)
    fkCustomerType: Mapped[str] = mapped_column(String)
    fkOrgParent: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    AutomaticPartDetailsEnabled: Mapped[bool] = mapped_column(Boolean)
    fkMpCountries: Mapped[str] = mapped_column(String)


class CustomerTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "CustomerTypes"

    Type: Mapped[str] = mapped_column(String(50))
    PartnerPfx: Mapped[int] = mapped_column(Integer)
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class DeliveryTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "DeliveryTypes"

    Type: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class DistributionTypes(Model):
    __bind_key__ = "access"
    __tablename__ = "DistributionTypes"

    Type: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class GpssPartNumberTranslation(Model):
    __bind_key__ = "access"
    __tablename__ = "GpssPartNumberTranslation"

    fkCustomerOrg: Mapped[str] = mapped_column(String)
    actualPartNumber: Mapped[str] = mapped_column(String(15))
    fictivePartNumber: Mapped[str] = mapped_column(String(15))
    Description: Mapped[str] = mapped_column(String(100))
    objVersion: Mapped[int] = mapped_column(Integer)
    changed: Mapped[datetime] = mapped_column(DateTime)
    price: Mapped[float] = mapped_column(Numeric, default=(0))


class InstalledLanguage(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledLanguage"

    fkInstalledPublication: Mapped[str] = mapped_column(String)
    fkLanguage: Mapped[str] = mapped_column(String)
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class InstalledPublication(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledPublication"

    PublicationTitle: Mapped[str] = mapped_column(String(50))
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class InstalledUpdate(Model):
    __bind_key__ = "access"
    __tablename__ = "InstalledUpdate"

    fkInstalledPublication: Mapped[str] = mapped_column(String)
    InstallDate: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    UpdateTitle: Mapped[str] = mapped_column(String(50))


class Languages(Model):
    __bind_key__ = "access"
    __tablename__ = "Languages"

    LanguageCode: Mapped[str] = mapped_column(String(50))
    Cid: Mapped[int] = mapped_column(Integer)
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class LexiconId_Descriptions(Model):
    __bind_key__ = "access"
    __tablename__ = "LexiconId_Descriptions"

    fkLanguage: Mapped[str] = mapped_column(String)
    Description: Mapped[str] = mapped_column(String(255))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class LexiconIds(Model):
    __bind_key__ = "access"
    __tablename__ = "LexiconIds"

    SourceEntity: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class MenuPricingCustomerOrgLabourRate(Model):
    __bind_key__ = "access"
    __tablename__ = "MenuPricingCustomerOrgLabourRate"

    fkCustomerOrg: Mapped[str] = mapped_column(String)
    price: Mapped[float] = mapped_column(Numeric)
    objVersion: Mapped[int] = mapped_column(Integer)
    Changed: Mapped[datetime] = mapped_column(DateTime)


class MenuPricing_MarketFactor(Model):
    __bind_key__ = "access"
    __tablename__ = "MenuPricing_MarketFactor"

    fkCountries: Mapped[str] = mapped_column(String)
    factor: Mapped[int] = mapped_column(Integer)
    objVersion: Mapped[int] = mapped_column(Integer)
    changed: Mapped[datetime] = mapped_column(DateTime)


class PartnerGroups(Model):
    __bind_key__ = "access"
    __tablename__ = "PartnerGroups"

    PartnerGroupCode: Mapped[str] = mapped_column(String(10))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class PublicationLanguage(Model):
    __bind_key__ = "access"
    __tablename__ = "PublicationLanguage"

    fkPublication: Mapped[str] = mapped_column(String)
    fkLanguage: Mapped[str] = mapped_column(String)
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

    Type: Mapped[str] = mapped_column(String(10))
    Description: Mapped[str] = mapped_column(String(50))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class Publications(Model):
    __bind_key__ = "access"
    __tablename__ = "Publications"

    fkPublicationType: Mapped[str] = mapped_column(String)
    PublicationTitle: Mapped[str] = mapped_column(String(50))
    Info: Mapped[str] = mapped_column(String(200))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    ParentPublicationTitle: Mapped[str] = mapped_column(String(50))


class RecentVINs(Model):
    __bind_key__ = "access"
    __tablename__ = "RecentVINs"

    VIN: Mapped[str] = mapped_column(String(20))
    fkUser: Mapped[str] = mapped_column(String)
    fkRecentVinOverridden: Mapped[str] = mapped_column(String)
    chassisNumber: Mapped[str] = mapped_column(String(10))
    registrationNumber: Mapped[str] = mapped_column(String(20))
    fkPartnerGroup: Mapped[int] = mapped_column(Integer)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class RecentVinOverridden(Model):
    __bind_key__ = "access"
    __tablename__ = "RecentVinOverridden"

    fkVehicleModel: Mapped[int] = mapped_column(Integer)
    fkModelYear: Mapped[int] = mapped_column(Integer)
    fkEngine: Mapped[int] = mapped_column(Integer)
    fkTransmission: Mapped[int] = mapped_column(Integer)


class ServerConfig(Model):
    __bind_key__ = "access"
    __tablename__ = "ServerConfig"

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

    fkInstalledPublication: Mapped[str] = mapped_column(String)
    fkInstalledUpdate: Mapped[str] = mapped_column(String)
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

    SessionId: Mapped[str] = mapped_column(String(50))


class UserRoles(Model):
    __bind_key__ = "access"
    __tablename__ = "UserRoles"

    fkCustomerType: Mapped[str] = mapped_column(String)
    Role: Mapped[str] = mapped_column(String(50))
    fkLexiconId: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class User_DMSSettings(Model):
    __bind_key__ = "access"
    __tablename__ = "User_DMSSettings"

    dmsKey: Mapped[str] = mapped_column(String(50))
    dmsValue: Mapped[str] = mapped_column(String(50))


class User_PersonalComments(Model):
    __bind_key__ = "access"
    __tablename__ = "User_PersonalComments"

    fkUserId: Mapped[str] = mapped_column(String(50))
    TargetElementId: Mapped[str] = mapped_column(String(50))
    TargetTypeId: Mapped[int] = mapped_column(Integer)
    CommentBody: Mapped[str] = mapped_column(String(500))
    CreationDate: Mapped[datetime] = mapped_column(DateTime)
    ModifiedDate: Mapped[datetime] = mapped_column(DateTime)


class User_Settings(Model):
    __bind_key__ = "access"
    __tablename__ = "User_Settings"

    SettingKey: Mapped[str] = mapped_column(String(50))
    SettingValue: Mapped[str] = mapped_column(String(50))


class User_ShoppingListParts(Model):
    __bind_key__ = "access"
    __tablename__ = "User_ShoppingListParts"

    fkShoppingList: Mapped[int] = mapped_column(Integer)
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

    fkUser: Mapped[str] = mapped_column(String(50))
    ShoppingListName: Mapped[str] = mapped_column(String(50))
    ShoppingListNumber: Mapped[int] = mapped_column(Integer, default=0)
    Changed: Mapped[datetime] = mapped_column(DateTime)


class Users(Model):
    __bind_key__ = "access"
    __tablename__ = "Users"

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
    fkAdminRule: Mapped[str] = mapped_column(String)
    fkCustomerOrg: Mapped[str] = mapped_column(String)
    fkUserRoles: Mapped[str] = mapped_column(String)
    fkLanguage: Mapped[str] = mapped_column(String)
    fkPartnerGroup: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)
    fkUserPermission: Mapped[str] = mapped_column(String)
    IsPriceWithVAT: Mapped[bool] = mapped_column(Boolean, default=1)
    DMSURLVOW: Mapped[str] = mapped_column(String(200))


class VinPartnerGroupCountries(Model):
    __bind_key__ = "access"
    __tablename__ = "VinPartnerGroupCountries"

    fkCountry: Mapped[str] = mapped_column(String)
    fkVinPartnerGroup: Mapped[str] = mapped_column(String)
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class VinPartnerGroups(Model):
    __bind_key__ = "access"
    __tablename__ = "VinPartnerGroups"

    VinPartnerGroupCode: Mapped[str] = mapped_column(String(50))
    fkPartnerGroup: Mapped[int] = mapped_column(Integer)
    decodePos9: Mapped[str] = mapped_column(String(1))
    Changed: Mapped[datetime] = mapped_column(DateTime)
    ObjVersion: Mapped[int] = mapped_column(Integer)


class WorkList(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList"

    listTitle: Mapped[str] = mapped_column(String(50))
    orderNumber: Mapped[str] = mapped_column(String(50))
    fkUserIdCreatedBy: Mapped[int] = mapped_column(Integer)
    listType: Mapped[str] = mapped_column(String(50), default="NONE")
    fkUserIdLockedBy: Mapped[int] = mapped_column(Integer)
    comment: Mapped[str] = mapped_column(String(-1))
    fkWorkList_Vehicle: Mapped[int] = mapped_column(Integer)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    version: Mapped[int] = mapped_column(Integer, default=1)
    partnerId: Mapped[str] = mapped_column(String(50))


class WorkList_Csc(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Csc"

    fkWorkList: Mapped[int] = mapped_column(Integer)
    csc: Mapped[str] = mapped_column(String(2))
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    qbNumber: Mapped[str] = mapped_column(String(7))
    qbDescription: Mapped[str] = mapped_column(String(20))


class WorkList_CscText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_CscText"

    fkCsc: Mapped[int] = mapped_column(Integer)
    isoLanguage: Mapped[str] = mapped_column(String(5))
    componentFunction: Mapped[str] = mapped_column(String(255))
    component: Mapped[str] = mapped_column(String(255))
    deviation: Mapped[str] = mapped_column(String(255))
    comment1: Mapped[str] = mapped_column(String(255))
    comment2: Mapped[str] = mapped_column(String(255))


class WorkList_Operation(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation"

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

    fkOperationTitle: Mapped[int] = mapped_column(Integer)
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(255))


class WorkList_Operation_List(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation_List"

    fkWorkList_Operation: Mapped[int] = mapped_column(Integer)


class WorkList_Operation_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Operation_Package"

    fkWorkList_Operation: Mapped[int] = mapped_column(Integer)


class WorkList_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Package"

    fkWorkList: Mapped[int] = mapped_column(Integer)
    packageNumber: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column(Integer)
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    usingFixedPrice: Mapped[bool] = mapped_column(Boolean)


class WorkList_PackageText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PackageText"

    fkPackageTitle: Mapped[int] = mapped_column(Integer)
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(1000))


class WorkList_Part(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part"

    partNumber: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[float] = mapped_column(Numeric)
    software: Mapped[bool] = mapped_column(Boolean)
    makeCode: Mapped[str] = mapped_column(String(5))
    jobNumber: Mapped[str] = mapped_column(String(50))
    dmsText: Mapped[str] = mapped_column(String(255))
    price: Mapped[float] = mapped_column(Numeric)
    fkWorkList_Vehicle: Mapped[int] = mapped_column(Integer)


class WorkList_PartText(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PartText"

    fkPartTitle: Mapped[int] = mapped_column(Integer)
    isoLanguage: Mapped[str] = mapped_column(String(10))
    text: Mapped[str] = mapped_column(String(255))


class WorkList_Part_List(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part_List"

    fkWorkList_Part: Mapped[int] = mapped_column(Integer)


class WorkList_Part_Package(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Part_Package"

    fkWorkList_Part: Mapped[int] = mapped_column(Integer)


class WorkList_PostponedQb(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_PostponedQb"

    fkWorkList: Mapped[int] = mapped_column(Integer)
    qbNumber: Mapped[str] = mapped_column(String(7))
    qbDescription: Mapped[str] = mapped_column(String(20))


class WorkList_Settings(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Settings"

    fkWorkListUser: Mapped[int] = mapped_column(Integer)
    settingName: Mapped[str] = mapped_column(String(50))
    settingValue: Mapped[str] = mapped_column(String(50))


class WorkList_User(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_User"

    userId: Mapped[str] = mapped_column(String(50))
    partnerId: Mapped[str] = mapped_column(String(50))
    idSelectedWorkList: Mapped[int] = mapped_column(Integer)


class WorkList_Vehicle(Model):
    __bind_key__ = "access"
    __tablename__ = "WorkList_Vehicle"

    profileId: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    vin: Mapped[str] = mapped_column(String(17))

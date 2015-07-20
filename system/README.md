### NEC Terrain system and its components

I did some research and present here lists of apps which should be left in the system,
which I have disabled and which I installed in order to replace stock or add functionality.

These lists reflect my **personal** opinion which can differ with yours. You should not blame me for this.
Moreover, I'm not affiliated with any programmer/developer. Think for yourself before you disable and
especially remove packages.

Also note
that the information was taken from my digging inside the phone. Do not get it as
100% correct, better check.

As an assurance, any statement below has been verified by me and not just copy-pasted from another internet source.
Currently in my phone all apps from the `disable` list below are indeed disabled and I confirm that:
* the phone boots
* it works normally
* it makes and receives calls
* the same for sms-s
* works with wifi
* data connection 4G works
* both main and front cameras and microphone work
* charging goes as expected
* external sd-card is accessible
* syncing with google account does not produce errors
* all expected programs autostart
* etc

*`enable` and `disable` lists together have absolutely __all__ packages which are initially in the system*

#### Apps from the stock rom which I left and why, aka `enable` list (raw list of packages in `apkensys`)

* android=/system/framework/framework-res.apk

  very system

* com.android.bluetooth=/system/app/Bluetooth.apk

  very system - bt
  
* com.android.certinstaller=/system/app/CertInstaller.apk

  very system - about certificates, seems important
  
* com.android.contacts=/system/app/Contacts.apk

  very system! This app is used not only to show, but also to add contacts. If you disable it, you cannot add contacts to your phone storage anymore because
  even any replacement app uses the interface of this one. It provides some *service* or *transport* to do this as I understand. Already stored contacts can be viewed, however. 
  If you still insist to disable/remove this one, you *will* have to install an alternative dialer at least
  as the stock dialer will disappear from any graphical view (but will be still enabled though). And again, no contacts cam be added to the phone storage.
  Note, that this program *does not start* if you disable/remove `com.android.att.settings.provider` but its part for adding contacts to the phone storage
  will still function properly if being called from a third-party program.
  
  I however wanted to avoid this app (`contacts`, I mean) as much as I can because I'm fed up with the fact that anytime I start it,
  it communicates to the internet switching data connection on, at least
  for few secs, even if there is wifi and even if before the data connection was off.
  
  So, since I have failed so far to disable this app I did like that:
  * I installed **DW Contacts**, which has a dialer as well
  * I disabled `com.android.att.settings.provider` and this automatically closed for me the full stock `contacts` (but not disabled)
  * Now I use **DW Contacts** to make calls. The actual call is made again using the stock `Phone` program internals, its graphics
  * When I add contacts in **DW Contacts** I see the interface of original `contacts`
  * BUT the data-connection has gone!
  
  The downside: if you try to start `contacts`, you see `unfortunately contacts has stopped`

* com.android.defcontainer=/system/app/DefaultContainerService.apk

  very system, looks like
  
* com.android.keychain=/system/app/KeyChain.apk

  very system, looks like
  
* com.android.launcher=/system/app/Launcher2.apk

  very system, looks like
  
* com.android.nfc=/system/app/Nfc.apk

  I guess this and next can be disabled if you do not need NFC, which eats your bettery, I left for a moment, do not know why
  
* com.android.nfchiddenmenu=/system/app/NfcHiddenMenu.apk

  I guess this and previous can be disabled if you do not need NFC, which eats your bettery, I left for a moment, do not know why
  
* com.android.packageinstaller=/system/app/PackageInstaller.apk

  **__EDIT:__** it is required by `pm` in the shell and `pm` does not operate w/o it, so do not remove

* com.android.phone=/system/app/Phone.apk

  You will not be able to make calls w/o this. It is not just graphics, also some binary internals to communicate with the modem, proprietary in fact. So, no replacement
  
* com.android.providers.applications=/system/app/ApplicationsProvider.apk

  Removing this will disintegrate your system. It may start, perhaps, but apps will not communicate one to each other. This is generically bad and causes many to complain or function improperly
  
* com.android.providers.contacts=/system/app/ContactsProvider.apk

  This is about the phone contacts storage, if disabled, no contacts to the phone can be stored
  
* com.android.providers.downloads=/system/app/DownloadProvider.apk

  Some settings for downloads, not sure it is really critical, but seems that some apps like playstore rely on it and do not bother themselves about where to store what
  
* com.android.providers.downloads.ui=/system/app/DownloadProviderUi.apk

  It is to see graphically, what and where has been saved, perhaps can be disabled/removed
  
* com.android.providers.drm=/system/app/DrmProvider.apk

  **not sure** what exactly this guy stores, but some databases look like mime-types identification
  
* com.android.providers.media=/system/app/MediaProvider.apk

  A centralized databse about where media files are, so that players see them all
  
* com.android.providers.settings=/system/app/SettingsProvider.apk

  **not sure** what exactly this guy stores, but looks important
  
* com.android.providers.telephony=/system/app/TelephonyProvider.apk

  The database which identifies a numeric gsm network id with the name. Maybe not really critical but chances are some interface elements may complain. They want to write a name, not a number of the
  gsm network
  
* com.android.providers.userdictionary=/system/app/UserDictionaryProvider.apk

  **__EDIT:__** If you remove this program you will get error `stop` anytime you quit editing of the input method properties. I decided to keep

* com.android.provision=/system/app/Provision.apk

  People say, it is important and its data look so, but not sure, what is it exactly
  
* com.android.settings=/system/app/Settings.apk

  Your setting interface
  
* com.android.smspush=/system/app/WAPPushManager.apk

  It is said to be realted to tethering operation, did not check myself inside
  
* com.android.stk=/system/app/Stk.apk

  Looks system
  
* com.android.systemui=/system/app/SystemUI.apk

  Looks system, the main graphical interface in fact
  
* com.android.vending=/data/app/com.android.vending-2.apk

  Looks system and is related to playservices
  
* com.android.vpndialogs=/system/app/VpnDialogs.apk

  Used for vpns and perhaps can be disabled/removed, if you are sure that vpn is not for you. Or may be there are better replacements
  
* com.google.android.apps.maps=/data/app/com.google.android.apps.maps-1.apk

  Google maps, I like
  
* com.google.android.gms=/data/app/com.google.android.gms-1.apk

  Needed for hangouts, which I need, and for other google apps, like maps, if their (google) description is correct
  
* com.google.android.gsf=/system/app/GoogleServicesFramework.apk

  google-service-framework, sounds system
  
* com.google.android.gsf.login=/system/app/GoogleLoginService.apk

  google-service-framework addition, sounds system
  
* com.google.android.location=/system/app/NetworkLocation.apk

  Location service, needed for maps w/o gps, or maybe with gps either
  
* com.google.android.onetimeinitializer=/system/app/OneTimeInitializer.apk

  Not used at all but one time when playstore is initialized, so if you will replay your system from zero, it should be in place
  
* com.google.android.street=/system/app/Street.apk

  Street view, useful
  
* com.google.android.syncadapters.contacts=/system/app/GoogleContactsSyncAdapter.apk

  Sync of your contacts to the google account
  
* com.google.android.talk=/data/app/com.google.android.talk-1.apk

  hangouts, I have to use it because of my colleagues
  
* com.ipsec.vpnclient=/system/app/VpnClient.apk

  VPN client, I can easily use it, but may be it is crappy and replaceable, I do not know
  
* com.kpt_nec.adaptxt=/system/app/NEC_Adaptxt_Base_v1_2.apk

  **__EDIT:__** IT IS VERY SYSTEM, It is what manges properties of your physical keyboard. The story is even more frustrating here:
  
  A virtual keyboard cannot be installed so you are in stuck in two situations:
  * You need some non-only-26-Latin-character input
  * You need to use something like terminal and to send, say ctrl-c, or arrow-up codes there
  
  I have tested dozens of options: no keyboard/input method starts its graphical interface. All silently use the physical keys and only them. `hackers keyboard` and `swiftkeyboard`
  are just two examples. If you go brave and **disable** `adaptxt` (of course installing some other input method in parallel and enabling it, and defaulting to it),
  then before reboot your keyboard will function but then you will the the so called boot loop. I got and it was tricky to get out.
  
  In fact it is a problem. How to use a terminal or type, for me for example, Cyrillic letters?

* com.nec.android.ncmc.ecomode=/system/app/EcoMode.apk

  ECO-mode, nec specific. Seems it can be off here, but I kept, let it save battery, maybe. Not sure, it is useful, though

* com.quicinc.fmradio=/system/app/FM.apk

  Perhaps crappy and replaceable but for me enough for the moment

#### App strangely not from the stock rom which **MUST** be there. Do not know why it is absent originally (also listed in `apkensys`)

* com.koushikdutta.superuser=/system/app/Superuser.apk

  *SUperuser, I need. Of course, it was __not__ in stock, but I put it before in the rom by hands*

#### Apps from the stock rom which I **disabled** and why, aka `disable` list (raw list of packages in `apkdissys`)

* borqs.soundrecorder=/system/app/SoundRecorder.apk

  It is the sound recorder, crappy and replaceable
  
* com.amazon.kindle=/system/app/KindleForAndroid-0.9.11-STUB.apk

  It is the kindle, why, even if I like reading, the screen is tiny for that
  
* com.android.DeviceHelp=/system/app/DeviceHelp.apk

  I do not need this, better use my laptop for help
  
* com.android.apps.tag=/system/app/Tag.apk

  **unknown** but removing did not cause troubles
  
* com.android.att.settings.provider=/system/app/ATTSettingsProvider.apk

  This **can** be removed but then ATT soft update does not work and stock `contacts` do not start. However, `contacts` **SHOULD NOT BE TOUCHED**, see in the list of still enabled apps why
  
* com.android.backupconfirm=/system/app/BackupRestoreConfirmation.apk

  Most likely related to a backup of *data*, not *settings* to your on-line (gmail) account. Not needed for me
  
* com.android.browser=/system/app/Browser.apk

  Stock crappy browser, there is firefox
  
* com.android.calculator2=/system/app/Calculator.apk

  Stock useless calculator
  
* com.android.calendar=/system/app/Calendar.apk

  Stock poor calendar
  
* com.android.chrome=/system/app/Chrome.apk

  Chrome, which I disfavor in view of Firefox
  
* com.android.contacts.map=/system/app/ContactMap.apk

  This to show a location of your contact given a zip code. Useless for me
  
* com.android.deskclock=/system/app/DeskClock.apk

  Crappy stock desktop clock
  
* com.android.email=/system/app/Email.apk

  Annoying stock e-mail, there is K-9
  
* com.android.facelock=/system/app/FaceLock.apk

  face-lock: I'm not crazy to trust it. Passwords only
  
* com.android.gallery3d=/system/app/Gallery2.apk

  It is the stock gallery, there are better and smaller around
  
* com.android.htmlviewer=/system/app/HTMLViewer.apk

  Not sure why, but removing it cause no issues
  
* com.android.magicsmoke=/system/app/MagicSmokeWallpapers.apk

  Wallpaper to eat you battery
  
* com.android.mms=/system/app/Mms.apk

  Stock sms/mms. The only feature it has compared to conquerers - managing sim-card sms. Used to be the fact in around 1995-2005
  
* com.android.music=/system/app/Music.apk

  Stock music player. There is VLC
  
* com.android.musicfx=/system/app/MusicFX.apk

  Stock music player enhancement. There is VLC
  
* com.android.musicvis=/system/app/VisualizationWallpapers.apk

  Wallpaper to eat you battery
  
* com.android.noisefield=/system/app/NoiseField.apk

  Wallpaper to eat you battery, if I'm not mistaken, removal is issue-free
  
* com.android.phasebeam=/system/app/PhaseBeam.apk

  Wallpaper to eat you battery
  
* com.android.protips=/system/app/Protips.apk

  Home screen tips, a la "tap here", I do not need
  
* com.android.providers.attxmlprovider=/system/app/ATTXmlProvider.apk

  ATT stuff but even w/o it `contacts` and connection to soft update worked, so why
  
* com.android.providers.calendar=/system/app/CalendarProvider.apk

  Stock calendar storage, but I do not want this calendar
  
* com.android.providers.partnerbookmarks=/system/app/PartnerBookmarksProvider.apk

  **unknown** but seems to be some advert, removed w/o issues
  
* com.android.sharedstoragebackup=/system/app/SharedStorageBackup.apk

  **__EDIT:__** this program can be removed and was misatkenly said as impoartant earlier

* com.android.videoeditor=/system/app/VideoEditor.apk

  Stock video editor, why
  
* com.android.voicedialer=/system/app/VoiceDialer.apk

  Stock voice-dialer, i.e. giving the contact to call by voice, not for me
  
* com.android.wallpaper=/system/app/LiveWallpapers.apk

  Wallpaper management to eat you battery
  
* com.android.wallpaper.holospiral=/system/app/HoloSpiralWallpaper.apk

  Wallpaper to eat you battery
  
* com.android.wallpaper.livepicker=/system/app/LiveWallpapersPicker.apk

  Wallpaper picker to eat you battery
  
* com.att.eptt=/system/app/EPTTVPL.apk

  In particular *eptt* pronounced in my native language means kind of "mother f&#ker", and it is. Some functionality to use some att service, I'm in Europe
  
* com.att.myWireless=/system/app/myATT_VPL_v5.apk

  I think to connect to att hotspots, I'm in Europe
  
* com.borqs.camera=/system/app/BorqsCamera.apk

  Stock camera, crappy
  
* com.borqs.dm=/system/app/DeviceManagement.apk

  Some device management, perhaps to use borqs apps with camera and sd card. No camera soft - nothing to manage
  
* com.borqs.exif=/system/app/Exif.apk

  Used in gallery to decipher photo metadata. I removed this gallery, so no use
  
* com.borqs.facebooksyncadapter=/system/app/FacebookSyncProvider.apk

  Send your photo to facebook, but no camera soft from borqs already
  
* com.borqs.filemanager=/system/app/BorqsFileManager.apk

  Perhaps, to list photos in the gallery which I removed, no other use found
  
* com.borqs.flickr=/system/app/Flickr.apk

  Send your photo to flickr, but no camera soft from borqs already
  
* com.borqs.gif=/system/app/Gif.apk

  Make animated gifs, or play them, I do not care, there are better apps for this
  
* com.borqs.hotspot=/system/app/hotspot.apk

  Some collection of us-based hotspot addresses, I'm in Europe
  
* com.borqs.movie=/system/app/BorqsVideoPlayer.apk

  To play your clips. There is VLC
  
* com.borqs.sdaccess=/system/app/DeviceManagementSDAccess.apk

  sdcard access to manage photos, only for this, other apps do it on their own - disable/remove safely
  
* com.borqs.tasks=/system/app/Tasks.apk

  task lists for you, quite poor. This app demands `Exchange` to be. Why?
  
* com.borqs.twittersync=/system/app/TwitterSyncProvider.apk

  Send your photo to twitter, but no camera soft from borqs already
  
* com.borqs.weatherwidget=/system/app/Weather_Widget.apk

  Widget is fine with me but it gets weather from an us-based system. I'm in Europe with other meteo facilities nearby
  
* com.cequint.ecid=/system/app/CityID-release.apk

  Says, in which city you are. Are you so drunk?
  
* com.drivemode=/system/app/DriveMode_1_0_2_3.apk

  To stop your phone from calling if you drive. And even if you are not, but just in a train
  
* com.google.android.apps.books=/system/app/BooksTablet.apk

  Books, in Terrain case on a screen less then your bankcard
  
* com.google.android.apps.plus=/system/app/PlusOne.apk

  G+, not for me
  
* com.google.android.apps.uploader=/system/app/MediaUploader.apk

  To upload your media to google drive, not for me
  
* com.google.android.backup=/system/app/GoogleBackupTransport.apk

  It is about *data* backup, not *settings* or contacts backup.
  
* com.google.android.feedback=/system/app/GoogleFeedback.apk

  It is to say, how crappy is google for you
  
* com.google.android.gm=/system/app/Gmail.apk

  gmail, Not for me, there is K-9
  
* com.google.android.googlequicksearchbox=/system/app/GoogleQuickSearchBox.apk

  Search widget on your screen, I search in firefox
  
* com.google.android.marvin.talkback=/system/app/talkback.apk

  If you are alone and want someone speak to you, phone in this case
  
* com.google.android.music=/system/app/Music2.apk

  Play music, there is VLC
  
* com.google.android.partnersetup=/system/app/GooglePartnerSetup.apk

  Adverts for google partners
  
* com.google.android.syncadapters.bookmarks=/system/app/ChromeBookmarksSyncAdapter.apk

  Synchronize chrome bookmarks, but I do not use chrome
  
* com.google.android.syncadapters.calendar=/system/app/GoogleCalendarSyncAdapter.apk

  synchronize your stock calendar with google, but I do not use the stock calendar
  
* com.google.android.tts=/system/app/GoogleTTS.apk

  text-to-speech, if you cannot read. But then anyway, Terrain's screen size is not for you
  
* com.google.android.videos=/system/app/Videos.apk

  Video player, there is VLC
  
* com.google.android.voicesearch=/system/app/VoiceSearch.apk

  Search with voice. I'm not crazy to talk to my phone
  
* com.google.android.youtube=/system/app/YouTube.apk

  Youtube, firefox plays youtube, so why
  
* com.matchboxmobile.wisp=/system/app/WISPr_58_Android22_postpaid.apk

  Some adverts for us-based service providers, I'm in Europe
  
* com.moxier.eas=/system/app/Exchange_mx.apk

  Exchange server interaction. Stock `Tasks` do not start without it
  
* com.mtag.att.codescanner=/system/app/ATT_code_scanner_vpl_1.2_aligned.apk

  att code-scanner, maybe it works in us better, but here in Europe not at all
  
* com.qo.android.sp.oem=/system/app/Quickoffice_Casio_SP_5.0.114_EC.apk

  Quick office discontinued, there are alternatives, I use andropen
  
* com.synchronoss.dcs.att.r2g=/system/app/ATT_Ready2Go.apk

  This is to help you screw up your phone, initial initialization
  
* com.telenav.app.android.cingular=/system/app/tn74-android-att-7400094.apk

  Some strange app in view of totally free navit
  
* com.wildtangent.android=/system/app/ATT_AndroidGames.apk

  I do not play, but would I, not these games
  
* com.yellowpages.android.ypmobile=/system/app/YPmobile-P-V3-8-1_B3539.apk

  yp for us mainly, as I got. Anyway, I can type `yellowpages` in firefox
  
* org.simalliance.openmobileapi.service=/system/app/SmartcardService.apk

  Some smartcard service, usage **unknown**. Some sources claim it is a part of security interaction in the phone.
  I checked: I could change PIN and use PUK with this app disabled, my android password active and works. So what?
  
* search.borqssearch=/system/app/BorqsSearchApp.apk

  **unknown**, but perhaps used by other borqs stuff, removed w/o issues

One comment: applications having `provider` in the name just contains some settings, or store data. The name suggest, which. If `calendar` it means that calendar
data are there. You should be careful disabling/removing such providers. Some third-party programs which tend to replace stock ones replace *only* the interface,
but continue using these *providers*. Some apps, however initiate their own storages. This is better, I guess
  
#### Apps which I **put to replace and to improve and/or to extend** the stock, which and why (raw list of packages in `apken3`)

* be.irm.kmi.meteo=/data/app/be.irm.kmi.meteo-1.apk

  Weather - Belgian meteo institute
  
* com.adobe.reader=/data/app/com.adobe.reader-1.apk

  Adobe reader instead of quick-office pdf
  
* com.alensw.PicFolder=/data/app/com.alensw.PicFolder-1.apk

  Better gallery
  
* com.andronicus.ledclock=/data/app/com.andronicus.ledclock-1.apk

  Nice clock, can play alarm to the music strem and make it **LOUD** via external speakers
  
* com.andropenoffice=/mnt/asec/com.andropenoffice-1/pkg.apk

  openoffice for android instead of quick-office
  
* com.andrwq.recorder=/mnt/asec/com.andrwq.recorder-1/pkg.apk

  Nice voice recorder
  
* com.dw.contacts.free=/data/app/com.dw.contacts.free-1.apk

  DW contacts to eliminate data-connection with the stock one. And it is MUCH better
  
* com.flavionet.android.camera.pro=/data/app/com.flavionet.android.camera.pro-1.apk

  camera, paid, but just for me
  
* com.flavionet.android.cinema.pro=/data/app/com.flavionet.android.cinema.pro-1.apk

  video, paid, but just for me
  
* com.fsck.k9=/data/app/com.fsck.k9-1.apk

  e-mail, does it ALL
  
* com.jb.gosms=/mnt/asec/com.jb.gosms-1/pkg.apk

  ALL what you can imagine about sms/mms
  
* com.skype.raider=/mnt/asec/com.skype.raider-1/pkg.apk

  skype
  
* com.socialnmobile.dictapps.notepad.color.note=/mnt/asec/com.socialnmobile.dictapps.notepad.color.note-1/pkg.apk

  very nice note-taker
  
* com.whatsapp=/data/app/com.whatsapp-1.apk

  watsapp
  
* jackpal.androidterm=/mnt/asec/jackpal.androidterm-1/pkg.apk

  terminal emulator - the must for me with android
  
* joa.zipper.editor=/data/app/joa.zipper.editor-1.apk

  nice text editor, a la gedit
  
* jp.co.johospace.jorte=/data/app/jp.co.johospace.jorte-1.apk

  extremely nice calendar+tasks organizer
  
* org.joa.zipperplus7v2=/mnt/asec/org.joa.zipperplus7v2-1/pkg.apk

  extreme file manager, including everything, even archiver, if I'm correct
  
* org.mozilla.firefox=/mnt/asec/org.mozilla.firefox-1/pkg.apk

  firefox
  
* org.navitproject.navit=/mnt/asec/org.navitproject.navit-1/pkg.apk

  navit - offline navigator with absolutely free and extreme quality weekly updated maps
  
* org.videolan.vlc=/mnt/asec/org.videolan.vlc-1/pkg.apk

  vlc - plays everything what can sound or be viewed
  
* uk.co.nickfines.RealCalc=/mnt/asec/uk.co.nickfines.RealCalc-1/pkg.apk

  Nice and quite scientific calculator

#### Apps autostart

The thing is like that. Say, you use skype. When you start the phone and *before* any interaction with skype and *before* any external call/message you may notice that its presence has gone from accounts to be synced and all skype contacts are gone from the contacts list.

BUT, skype is alive, you can start chating from outside.

Once you interact with skype somehow (on the phone or chat/call from outside), all these oddities are gone.

Eventually I spotted the beast: it is like that if you have moved skype to the sd-card. I decided just to keep it in the phone, not a problem, but good to know. Perhaps this affect other programs of such kind.

*Most likely this effort is to be continued ...*

Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl):	Sun JDK - ¶rodowisko programistyczne Javy dla Linuksa
Name:		java-sun
Version:	1.5.0
Release:	0.beta3.1
License:	restricted, non-distributable
Group:		Development/Languages/Java
# download directly from http://java.sun.com/j2se/1.5.0/snapshots/index.jsp
%ifarch %{ix86}
Source0:	jdk-1_5_0-beta3-bin-b57-linux-i586-23_jun_2004.bin
# NoSource0-md5: ddbdcf7cde8d261f4ac975572e2b6d85
%endif
%ifarch amd64
Source0:	jdk-1_5_0-beta3-bin-b57-linux-amd64-23_jun_2004.bin
# NoSource0-md5: 70ba79bdbf8cd2ba62f0fb99058c0ee9
%endif
NoSource:	0
Patch0:		%{name}-ControlPanel-fix.patch
Patch1:		%{name}-desktop.patch
URL:		http://java.sun.com/linux/
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	unzip
Requires:	java-sun-jre = %{version}-%{release}
Provides:	jdk = %{version}
Provides:	j2sdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java-sun
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javadir		%{_libdir}/java
%define		jredir		%{_libdir}/java/jre
%define		_javalibdir	%{_datadir}/java
%define		netscape4dir	/usr/%{_lib}/netscape
%define		mozilladir	/usr/%{_lib}/mozilla
%define		firefoxdir	/usr/%{_lib}/mozilla-firefox


# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
# the rest is because -jdbc wants unixODBC-devel(?)
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libodbcinst.so' 'libodbc.so'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

%description
Java Development Kit for Linux.

%description -l pl
¦rodowisko programistyczne Javy dla Linuksa.

%package jdbc
Summary:	JDBC files for Sun Java
Summary(pl):	Pliki JDBC dla Javy Suna
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	libodbc.so.1
Requires:	libodbcinst.so.1

%description jdbc
This package contains JDBC files for Sun Java.

%description jdbc -l pl
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl):	Sun JRE - ¶rodowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	XFree86-libs
Requires:	java-shared
Provides:	java1.4
Provides:	jre = %{version}
Provides:	java
Provides:	javaws = %{version}
Provides:	jndi = %{version}
Provides:	jndi-ldap = %{version}
Provides:	jndi-cos = %{version}
Provides:	jndi-rmi = %{version}
Provides:	jndi-dns = %{version}
Provides:	jaas = %{version}
Provides:	jsse = %{version}
Provides:	jce = %{version}
Provides:	jdbc-stdext = 3.0
Provides:	jdbc-stdext = %{version}
Obsoletes:	jre
Obsoletes:	java-blackdown-jre
Obsoletes:	jndi
Obsoletes:	jndi-provider-ldap
Obsoletes:	jndi-provider-cosnaming
Obsoletes:	jndi-provider-rmiregistry
Obsoletes:	jndi-provider-dns
Obsoletes:	jaas
Obsoletes:	jsse
Obsoletes:	jce
Obsoletes:	jdbc-stdext

%description jre
Java Runtime Environment for Linux.

%description jre -l pl
¦rodowisko uruchomieniowe Javy dla Linuksa.

%package alsa
Summary:	JRE module for ALSA sound support
Summary(pl):	Modu³ JRE do obs³ugi d¼wiêku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}

%description alsa
JRE module for ALSA sound support.

%description alsa -l pl
Modu³ JRE do obs³ugi d¼wiêku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl):	Wspó³dzielone narzêdzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	jar
Provides:	java-shared
Obsoletes:	java-shared
Obsoletes:	jar
Obsoletes:	fastjar

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl
Pakiet ten zawiera narzêdzia wspólne dla ka¿dej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Obsoletes:	java-blackdown-demos
Obsoletes:	jdk-demos

%description demos
JDK demonstration programs.

%description demos -l pl
Programy demonstracyjne do JDK.

%package -n netscape4-plugin-%{name}
Summary:	Netscape 4.x Java plugin
Summary(pl):	Wtyczka Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin

%description -n netscape4-plugin-%{name}
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Netscape 4.x.

%package mozilla-plugin
Summary:	Mozilla Java plugin file
Summary(pl):	Plik wtyczki Javy do Mozilli
Group:		Development/Languages/Java
Requires:	jre = %{version}
Obsoletes:	java-blackdown-mozilla-plugin

%description mozilla-plugin
Java plugin file for Mozilla.

%description mozilla-plugin -l pl
Plik wtyczki z obs³ug± Javy dla Mozilli.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla Java plugin
Summary(pl):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
PreReq:		mozilla-embedded
Requires:	%{name}-mozilla-plugin = %{version}-%{release}
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun
Obsoletes:	mozilla-plugin-gcc2-java-sun
Obsoletes:	mozilla-plugin-gcc3-java-sun
Obsoletes:	mozilla-plugin-gcc32-java-sun

%description -n mozilla-plugin-%{name}
Java plugin for Mozilla compiled using gcc 3.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Mozilli skompilowana przy u¿yciu gcc 3.

%package -n mozilla-firefox-plugin-%{name}
Summary:	Mozilla Firefox Java plugin
Summary(pl):	Wtyczka Javy do Mozilli Firefox
Group:		Development/Languages/Java
PreReq:		mozilla-firefox
Requires:	%{name}-mozilla-plugin = %{version}-%{release}
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-gcc2-java-sun
Obsoletes:	mozilla-firefox-plugin-gcc3-java-sun

%description -n mozilla-firefox-plugin-%{name}
Java plugin for Mozilla Firefox compiled using gcc 3.

%description -n mozilla-firefox-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Mozilli Firefox skompilowana przy u¿yciu gcc 3.

%prep
%setup -q -T -c -n jdk%{version}
cd ..
export MORE=10000
sh %{SOURCE0} <<EOF
yes
EOF
cd jdk%{version}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{_javalibdir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/{,ja/}man1

cp -rf bin demo include lib $RPM_BUILD_ROOT%{javadir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

if test -f jre/lib/i386/client/Xusage.txt ; then
mv -f jre/lib/i386/client/Xusage.txt jre/Xusage.client
fi
if test -f jre/lib/i386/server/Xusage.txt ; then
mv -f jre/lib/i386/server/Xusage.txt jre/Xusage.server
fi
if test -f jre/lib/*.txt ; then
mv -f jre/lib/*.txt jre
fi
#mv jre/lib/font.properties{,.orig}
#mv jre/lib/font.properties{.Redhat6.1,}

cp -rf jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

# conflict with heimdal
for i in kinit klist ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/j$i
	mv -f $RPM_BUILD_ROOT%{_mandir}/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/man1/j${i}.1
	mv -f $RPM_BUILD_ROOT%{_mandir}/ja/man1/${i}.1 $RPM_BUILD_ROOT%{_mandir}/ja/man1/j${i}.1
done

for i in ControlPanel java java_vm keytool ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jdb native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

#for i in javaplugin rt sunrsasign ; do
#	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
#done

install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{firefoxdir}/plugins,%{jredir}/plugin/i386/ns7{,-gcc29}}
install jre/plugin/i386/ns7/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{jredir}/plugin/i386/ns7
ln -sf %{jredir}/plugin/i386/ns7/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins
ln -sf %{jredir}/plugin/i386/ns7/libjavaplugin_oji.so \
	$RPM_BUILD_ROOT%{firefoxdir}/plugins
install  -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install jre/plugin/desktop/*.desktop $RPM_BUILD_ROOT%{_desktopdir}
install jre/plugin/desktop/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

# these binaries are in %{jredir}/bin - not needed in %{javadir}/bin?
rm -f $RPM_BUILD_ROOT%{javadir}/bin/{ControlPanel,keytool,kinit,klist,ktab,orbd,policytool,rmid,rmiregistry,servertool,tnameserv}

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{_javalibdir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{_javalibdir}/jce.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-ldap.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-cos.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jndi-rmi.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jaas.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jdbc-stdext.jar
ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{_javalibdir}/jdbc-stdext-3.0.jar

install -d -m 755 $RPM_BUILD_ROOT%{jredir}/javaws
cp -a jre/javaws/* $RPM_BUILD_ROOT%{jredir}/javaws
perl -p -i -e 's#javaws\.cfg\.jre\.0\.path=.*#javaws\.cfg\.jre\.0\.path=%{jredir}/bin/java#' $RPM_BUILD_ROOT%{jredir}/javaws/javaws.cfg
ln -sf %{jredir}/javaws/javaws.jar $RPM_BUILD_ROOT%{_javalibdir}/javaws.jar
ln -sf %{jredir}/javaws/javaws-l10n.jar $RPM_BUILD_ROOT%{_javalibdir}/javaws-l10n.jar
mv -f $RPM_BUILD_ROOT{%{jredir}/lib,%{_datadir}}/locale

%find_lang sunw_java_plugin --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%pre jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE README.html
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%attr(755,root,root) %{javadir}/bin/appletviewer
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/apt
%attr(755,root,root) %{javadir}/bin/javaws
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jsadebugd
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%{javadir}/include
%dir %{javadir}/lib
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl
%{_mandir}/man1/appletviewer.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%{_mandir}/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/jconsole.1*


%files jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libJdbcOdbc.so

%files jre
%defattr(644,root,root,755)
%doc jre/{CHANGES,COPYRIGHT,LICENSE,README,Xusage*,*.txt}
%doc jre/Welcome.html
%attr(755,root,root) %{_bindir}/ControlPanel
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/jkinit
%attr(755,root,root) %{_bindir}/jklist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{jredir}/bin/javaws
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/unpack200
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/unpack200
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/ControlPanel
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/kinit
%attr(755,root,root) %{jredir}/bin/klist
%attr(755,root,root) %{jredir}/bin/ktab
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%{jredir}/lib/fonts
%attr(755,root,root) %{jredir}/lib/i386/client
%attr(755,root,root) %{jredir}/lib/i386/native_threads
%attr(755,root,root) %{jredir}/lib/i386/server
%{jredir}/lib/i386/jvm.cfg
%attr(755,root,root) %{jredir}/lib/i386/awt_robot
%attr(755,root,root) %{jredir}/lib/i386/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/i386/libjsoundalsa.so
%{jredir}/lib/im
%{jredir}/lib/images
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 size mtime) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
#%%{jredir}/lib/*.cfg
#%%{jredir}/lib/tzmappings
%lang(ja) %{jredir}/lib/*.properties.ja
##%lang(zh) %{jredir}/lib/*.properties.zh
%dir %{jredir}/plugin
%dir %{jredir}/plugin/i386
%dir %{_javalibdir}
%{_javalibdir}/jaas.jar
%{_javalibdir}/javaws*.jar
%{_javalibdir}/jce.jar
%{_javalibdir}/jcert.jar
%{_javalibdir}/jdbc-stdext*.jar
%{_javalibdir}/jndi*.jar
%{_javalibdir}/jnet.jar
%{_javalibdir}/jsse.jar
%{jredir}/lib/classlist
%{jredir}/lib/fontconfig.RedHat.2.1.bfc
%{jredir}/lib/fontconfig.RedHat.2.1.properties.src
%{jredir}/lib/fontconfig.RedHat.3.bfc
%{jredir}/lib/fontconfig.RedHat.3.properties.src
%{jredir}/lib/fontconfig.RedHat.8.0.bfc
%{jredir}/lib/fontconfig.RedHat.8.0.properties.src
%{jredir}/lib/fontconfig.RedHat.bfc
%{jredir}/lib/fontconfig.RedHat.properties.src
%{jredir}/lib/fontconfig.SuSE.bfc
%{jredir}/lib/fontconfig.SuSE.properties.src
%{jredir}/lib/fontconfig.Sun.2003.bfc
%{jredir}/lib/fontconfig.Sun.2003.properties.src
%{jredir}/lib/fontconfig.Sun.bfc
%{jredir}/lib/fontconfig.Sun.properties.src
%{jredir}/lib/fontconfig.Turbo.8.0.bfc
%{jredir}/lib/fontconfig.Turbo.8.0.properties.src
%{jredir}/lib/fontconfig.Turbo.bfc
%{jredir}/lib/fontconfig.Turbo.properties.src
%{jredir}/lib/fontconfig.bfc
%{jredir}/lib/fontconfig.properties.src
%attr(755,root,root) %{jredir}/lib/i386/gtkhelper
%attr(755,root,root) %{jredir}/lib/i386/headless/libmawt.so
%attr(755,root,root) %{jredir}/lib/i386/libsaproc.so
%attr(755,root,root) %{jredir}/lib/i386/libunpack.so
%attr(755,root,root) %{jredir}/lib/i386/motif21/libmawt.so
%attr(755,root,root) %{jredir}/lib/i386/xawt/libmawt.so
%{jredir}/lib/javaws/Java1.5.ico
%{jredir}/lib/javaws/messages.properties
%{jredir}/lib/javaws/messages_de.properties
%{jredir}/lib/javaws/messages_es.properties
%{jredir}/lib/javaws/messages_fr.properties
%{jredir}/lib/javaws/messages_it.properties
%{jredir}/lib/javaws/messages_ja.properties
%{jredir}/lib/javaws/messages_ko.properties
%{jredir}/lib/javaws/messages_sv.properties
%{jredir}/lib/javaws/messages_zh_CN.properties
%{jredir}/lib/javaws/messages_zh_HK.properties
%{jredir}/lib/javaws/messages_zh_TW.properties
%{jredir}/lib/javaws/miniSplash.jpg
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko.UTF-8) %{_datadir}/locale/ko.UTF-8/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh.GBK) %{_datadir}/locale/zh.GBK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh) %{_datadir}/locale/zh/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh) %{_datadir}/locale/zh_HK.BIG5HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh) %{_datadir}/locale/zh_TW.BIG5/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh) %{_datadir}/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
%{jredir}/lib/management/jmxremote.access
%{jredir}/lib/management/jmxremote.password.template
%{jredir}/lib/management/management.properties
%{jredir}/lib/management/snmp.acl.template
%{_desktopdir}/sun_java.desktop
%{_pixmapsdir}/sun_java.png
%{_mandir}/man1/java.1*
%{_mandir}/man1/javaws.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/jkinit.1*
%{_mandir}/man1/jklist.1*
%{_mandir}/man1/ktab.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/policytool.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%{_mandir}/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/jkinit.1*
%lang(ja) %{_mandir}/ja/man1/jklist.1*
%lang(ja) %{_mandir}/ja/man1/ktab.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*
%dir %{jredir}/javaws
##%{jredir}/javaws/resources
%attr(755,root,root) %{jredir}/javaws/javaws
##%attr(755,root,root) %{jredir}/javaws/javawsbin
##%{jredir}/javaws/cacerts
##%{jredir}/javaws/*.gif
##%{jredir}/javaws/*.jar
##%{jredir}/javaws/*.policy
##%{jredir}/javaws/*.html

%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/i386/libjsoundalsa.so

%files demos
%defattr(644,root,root,755)
%{javadir}/demo

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/rmic
%{_mandir}/man1/jar.1*
%{_mandir}/man1/rmic.1*
%{_mandir}/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*

%files mozilla-plugin
%defattr(644,root,root,755)
%dir %{jredir}/plugin/i386/ns7
%attr(755,root,root) %{jredir}/plugin/i386/ns7/libjavaplugin_oji.so

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%{mozilladir}/plugins/libjavaplugin_oji.so

%files -n mozilla-firefox-plugin-%{name}
%defattr(644,root,root,755)
%{firefoxdir}/plugins/libjavaplugin_oji.so

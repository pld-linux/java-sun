Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl):	Sun JDK - ¶rodowisko programistyczne Javy dla Linuksa
Name:		java-sun
Version:	1.4.0
Release:	0.2
License:	restricted, non-distributable
Group:		Development/Languages/Java
URL:		http://java.sun.com/linux/
Source0:	ftp://128.167.104.34/pub/j2sdk/1.4.0/poiu4rfpo4/j2sdk-1_4_0-linux-i386.bin
NoSource:	0
Provides:	jdk = %{version}
Requires:	java-sun-jre = %{version}
Obsoletes:	ibm-java
Obsoletes:	jdk
Obsoletes:	kaffe
BuildRequires:	unzip
BuildConflicts: ibm-java
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jdkdir		%{_libdir}/jdk%{version}
%define		jredir		%{_libdir}/jre%{version}
%define		netscape4dir	/usr/X11R6/lib/netscape
%define		mozilladir	/usr/X11R6/lib/mozilla

# ??? unixODBC-devel?
%define		_noautoreq	libodbcinst.so libodbc.so

%description
Java Development Kit for Linux.

%description -l pl
¦rodowisko programistyczne Javy dla Linuksa.

%package -n java-sun-jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl):	Sun JRE - ¶rodowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Provides:	java1.4
Provides:	jre
Provides:	jar
Provides:	java
Obsoletes:	jre
Requires:	XFree86-libs
Requires:	libstdc++-compat

%description -n java-sun-jre
Java Runtime Environment for Linux.

%description -n java-sun-jre -l pl
¦rodowisko uruchomieniowe Javy dla Linuksa.

%package -n java-sun-demos
Summary:	JDK demonstration programs
Summary(pl):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name} = %{version}
Obsoletes:	jdk-demos

%description -n java-sun-demos
JDK demonstration programs.

%description -n java-sun-demos -l pl
Programy demonstracyjne do JDK.

%package -n java-sun-nn4-plugin
Summary:	Netscape 4.x Java plugin
Summary(pl):	Plugin Javy do Netscape 4.x
Group:		Development/Languages/Java
Requires:	jre = %{version}
Requires:	netscape-common >= 4.0
Obsoletes:	jre-netscape4-plugin

%description -n java-sun-nn4-plugin
Java plugin for Netscape 4.x.

%description -n java-sun-nn4-plugin -l pl
Plugin z obs³ug± Javy dla Netscape 4.x.

%package -n java-sun-moz-plugin
Summary:	Mozilla Java plugin
Summary(pl):	Plugin Javy do Mozilli
Group:		Development/Languages/Java
Requires:	jre = %{version}
Requires:	mozilla
Obsoletes:	jre-mozilla-plugin

%description -n java-sun-moz-plugin
Java plugin for Mozilla.

%description -n java-sun-moz-plugin -l pl
Plugin z obs³ug± Javy dla Mozilli.

%prep
%setup -q -T -c -n j2sdk%{version}
cd ..
outname=install.sfx.$$
tail +295 %{SOURCE0} >$outname
chmod +x $outname
./$outname
rm $outname

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jdkdir},%{jredir},%{_bindir}} \
	$RPM_BUILD_ROOT{%{_includedir}/jdk,%{_mandir}/{,ja/}man1}

cp -rf bin demo lib $RPM_BUILD_ROOT%{jdkdir}
cp -rf include/* $RPM_BUILD_ROOT%{_includedir}/jdk
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1
ln -sf ../jre%{version} $RPM_BUILD_ROOT%{jdkdir}/jre
ln -sf ../../include/jdk $RPM_BUILD_ROOT%{jdkdir}/include

mv -f jre/lib/i386/client/Xusage.txt jre/Xusage.client
mv -f jre/lib/i386/server/Xusage.txt jre/Xusage.server
mv -f jre/lib/*.txt jre

cp -rf jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

for i in ControlPanel java java_vm keytool orbd policytool rmid rmiregistry \
         servertool tnameserv ; do
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in HtmlConverter appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jdb native2ascii rmic serialver ; do
	ln -sf %{jdkdir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

install -d $RPM_BUILD_ROOT%{netscape4dir}/{plugins,java/classes}
install jre/plugin/i386/ns4/javaplugin140.so $RPM_BUILD_ROOT%{netscape4dir}/plugins
for i in javaplugin rt sunrsasign ; do
	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
done

install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{jredir}/plugin/i386/ns610}
install jre/plugin/i386/ns610/libjavaplugin_oji140.so \
	$RPM_BUILD_ROOT%{jredir}/plugin/i386/ns610
ln -sf %{jredir}/plugin/i386/ns610/libjavaplugin_oji140.so \
	$RPM_BUILD_ROOT%{mozilladir}/plugins

gzip -9nf COPYRIGHT LICENSE README \
	jre/{CHANGES,COPYRIGHT,LICENSE,README,Xusage*,*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n java-sun-jre
/sbin/ldconfig -n %{jredir}/lib/i386

%files
%defattr(644,root,root,755)
%doc *.gz README.html
%attr(755,root,root) %{_bindir}/HtmlConverter
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{jdkdir}/bin
%{_includedir}/jdk
%dir %{jdkdir}/lib
%dir %{jdkdir}/lib/*.jar
%dir %{jdkdir}/lib/*.idl
%{jdkdir}/jre
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*

%files -n java-sun-jre
%defattr(644,root,root,755)
%doc jre/*.gz jre/Welcome.html jre/ControlPanel.html
%attr(755,root,root) %{_bindir}/ControlPanel
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{jredir}/bin
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext
%{jredir}/lib/fonts
%attr(755,root,root) %{jredir}/lib/i386
%{jredir}/lib/images
%{jredir}/lib/security
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
#%{jredir}/lib/*.cfg
#%{jredir}/lib/tzmappings
%lang(ja) %{jredir}/lib/*.properties.ja
#%lang(zh) %{jredir}/lib/*.properties.zh
%dir %{jredir}/plugin
%dir %{jredir}/plugin/i386

%files -n java-sun-demos
%defattr(644,root,root,755)
%{jdkdir}/demo

%files -n java-sun-nn4-plugin
%defattr(644,root,root,755)
%attr(755,root,root) %{netscape4dir}/plugins/javaplugin140.so
%{netscape4dir}/java/classes/*
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(es) %{jredir}/lib/locale/es
%lang(fr) %{jredir}/lib/locale/fr
%lang(it) %{jredir}/lib/locale/it
%lang(ja) %{jredir}/lib/locale/ja
%lang(ko) %{jredir}/lib/locale/ko
%lang(ko.UTF-8) %{jredir}/lib/locale/ko.UTF-8
%lang(sv) %{jredir}/lib/locale/sv
%lang(zh) %{jredir}/lib/locale/zh
%lang(zh.GBK) %{jredir}/lib/locale/zh.GBK
%lang(zh_TW) %{jredir}/lib/locale/zh_TW
%lang(zh_TW.BIG5) %{jredir}/lib/locale/zh_TW.BIG5

%files -n java-sun-moz-plugin
%defattr(644,root,root,755)
%dir %{jredir}/plugin/i386/ns610
%attr(755,root,root) %{jredir}/plugin/i386/ns610/libjavaplugin_oji140.so
%{mozilladir}/plugins/libjavaplugin_oji140.so

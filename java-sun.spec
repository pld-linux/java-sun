Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl):	Sun JDK - ¶rodowisko programistyczne Javy dla Linuksa
Name:		java-sun
Version:	1.4.1_02
Release:	0.1
License:	restricted, non-distributable
Group:		Development/Languages/Java
# download through forms from http://java.sun.com/
Source0:	j2sdk-1_4_1-src-scsl.zip
Patch0:         %{name}-bash.patch
Patch1:         %{name}-no_sanity.patch
Patch2:         %{name}-cpp.patch
Patch3:         %{name}-pthread.patch
Patch4:         %{name}-motif.patch
Patch5:         %{name}-fork.patch
Patch6:         %{name}-no_plugins.patch
NoSource:	0
URL:		http://java.sun.com/linux/
#Requires:	java-sun-jre = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
BuildREquires:	bash
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javadir		%{_libdir}/java
#%%define		jredir		%{_libdir}/java/jre
%define		classdir	%{_datadir}/java
#%%define		netscape4dir	/usr/lib/netscape
#%%define		mozilladir	/usr/lib/mozilla

# prevent wrong requires when building with another JRE
%define		_noautoreqdep	libawt.so libjava.so libjvm.so libmlib_image.so libverify.so libnet.so
# ??? unixODBC-devel?
%define		_noautoreq	libodbcinst.so libodbc.so

%description
Java Development Kit for Linux.

%description -l pl
¦rodowisko programistyczne Javy dla Linuksa.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl):	Sun JRE - ¶rodowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Provides:	java1.4
Provides:	jre = %{version}
Requires:	java-shared
#rovides:	jar
Provides:	java
Obsoletes:	jre
Obsoletes:	java-blackdown-jre
Requires:	XFree86-libs
Requires:	libstdc++-compat

%description jre
Java Runtime Environment for Linux.

%description jre -l pl
¦rodowisko uruchomieniowe Javy dla Linuksa.

%package tools
Summary:        Shared java tools
Summary(pl):    Wspó³dzielone narzêdzia javy
Group:          Development/Languages/Java
Provides:       jar
Provides:       java-shared
Obsoletes:	java-shared
Obsoletes:	jar
Obsoletes:      fastjar

%description tools
This package contains tools that are common for every Java(tm) implementation,
such as rmic or jar.

%description tools -l pl
Pakiet ten zawiera narzêdzia wspólne dla ka¿dej implementacji Javy(tm), takie
jak rmic czy jar.


%package demos

Summary:	JDK demonstration programs
Summary(pl):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}
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
Requires:	%{name}-jre = %{version}
Requires:	netscape-common >= 4.0
Obsoletes:	blackdown-java-sdk-netscape4-plugin
Obsoletes:	netscape4-plugin-java-blackdown
Obsoletes:	java-sun-nn4-plugin
Obsoletes:	jre-netscape4-plugin

%description -n netscape4-plugin-%{name}
Java plugin for Netscape 4.x.

%description -n netscape4-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Netscape 4.x.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla Java plugin
Summary(pl):	Wtyczka Javy do Mozilli
Group:		Development/Languages/Java
Requires:	jre = %{version}
Prereq:		mozilla-embedded
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-java-blackdown

%description -n mozilla-plugin-%{name}
Java plugin for Mozilla.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka z obs³ug± Javy dla Mozilli.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build

cd control/make

export RPM_OPT_FLAGS
make all DEV_ONLY=true \
        HOTSPOT_BUILD_JOBS=1 \
        ALT_BOOTDIR=/usr
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{javadir},%{classdir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT%{_mandir}/{,ja/}man1

cp -rf control/build/linux-i586/j2sdk-image/{bin,demo,include,lib} $RPM_BUILD_ROOT%{javadir}
cp -rf control/build/linux-i586/j2sdk-image/jre/lib $RPM_BUILD_ROOT%{javadir}
install control/build/linux-i586/j2sdk-image/man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install control/build/linux-i586/j2sdk-image/man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

# not needed now?
#ln -sf %{jredir} $RPM_BUILD_ROOT/usr/lib/jre
#ln -sf %{javadir}/include $RPM_BUILD_ROOT%{_includedir}/java

#mv -f jre/lib/i386/client/Xusage.txt jre/Xusage.client
#mv -f jre/lib/i386/server/Xusage.txt jre/Xusage.server
#mv -f jre/lib/*.txt jre
mv $RPM_BUILD_ROOT%{javadir}/lib/font.properties{,.orig}
mv $RPM_BUILD_ROOT%{javadir}/lib/font.properties{.Redhat6.1,}

#cp -rf jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

for i in java keytool kinit klist ktab orbd policytool \
	rmid rmiregistry servertool tnameserv ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in appletviewer extcheck idlj jar jarsigner java-rmi.cgi \
         javac javadoc javah javap jdb native2ascii rmic serialver ; do
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

#rm -f $RPM_BUILD_ROOT%{javadir}/bin/java
#ln -sf %{jredir}/bin/java $RPM_BUILD_ROOT%{javadir}/bin/java

#install -d $RPM_BUILD_ROOT%{netscape4dir}/{plugins,java/classes}
#install jre/plugin/i386/ns4/javaplugin.so $RPM_BUILD_ROOT%{netscape4dir}/plugins
#for i in javaplugin rt sunrsasign ; do
#	ln -sf %{jredir}/lib/$i.jar $RPM_BUILD_ROOT%{netscape4dir}/java/classes
#done

#install -d $RPM_BUILD_ROOT{%{mozilladir}/plugins,%{jredir}/plugin/i386/ns610}
#install jre/plugin/i386/ns610/libjavaplugin_oji.so \
#	$RPM_BUILD_ROOT%{jredir}/plugin/i386/ns610
#ln -sf %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so \
#	$RPM_BUILD_ROOT%{mozilladir}/plugins

## these binaries are in %{jredir}/bin - not needed in %{javadir}/bin?
#rm -f $RPM_BUILD_ROOT%{javadir}/bin/{ControlPanel,keytool,kinit,klist,ktab,orbd,policytool,rmid,rmiregistry,servertool,tnameserv}

%clean
rm -rf $RPM_BUILD_ROOT

#%pre jre
#if [ -L %{jredir} ]; then
#	rm -f %{jredir}
#fi
#if [ -L %{javadir} ]; then
#	rm -f %{javadir}
#fi

#%post jre
#/sbin/ldconfig -n %{jredir}/lib/i386

%files
%defattr(644,root,root,755)
#%%doc COPYRIGHT LICENSE README README.html
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
#attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{javadir}/bin/appletviewer
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jar
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/serialver
%{javadir}/include
#%%{_includedir}/jdk
%dir %{javadir}/lib
%{javadir}/lib/*.idl
%{_mandir}/man1/appletviewer.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jar.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
#lang(ja) %{_mandir}/ja/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*

%files jre
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/ktab
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/kinit
%attr(755,root,root) %{javadir}/bin/klist
%attr(755,root,root) %{javadir}/bin/ktab
%attr(755,root,root) %{javadir}/bin/orbd
%attr(755,root,root) %{javadir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/servertool
%attr(755,root,root) %{javadir}/bin/tnameserv
%dir %{javadir}/lib
%{javadir}/lib/applet
%{javadir}/lib/audio
%{javadir}/lib/cmm
%{javadir}/lib/ext
%{javadir}/lib/fonts
%attr(755,root,root) %{javadir}/lib/i386
%{javadir}/lib/im
%{javadir}/lib/images
%{javadir}/lib/security
%{javadir}/lib/zi
%{javadir}/lib/*.jar
%{javadir}/lib/*.properties
#%%{jredir}/lib/*.cfg
#%%{jredir}/lib/tzmappings
%lang(ja) %{javadir}/lib/*.properties.ja
##%lang(zh) %{jredir}/lib/*.properties.zh
#%dir %{javadir}/plugin
#%dir %{javadir}/plugin/i386
%dir %{classdir}
%{_mandir}/man1/java.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/policytool.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
#lang(ja) %{_mandir}/ja/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*

%files demos
%defattr(644,root,root,755)
%{javadir}/demo

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/rmic
%{_mandir}/man1/rmiregistry.1*
%{_mandir}/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*

#%files -n netscape4-plugin-%{name}
#%defattr(644,root,root,755)
#%attr(755,root,root) %{netscape4dir}/plugins/javaplugin.so
#%{netscape4dir}/java/classes/*
#%dir %{jredir}/lib/locale
#%lang(de) %{jredir}/lib/locale/de
#%lang(es) %{jredir}/lib/locale/es
#%lang(fr) %{jredir}/lib/locale/fr
#%lang(it) %{jredir}/lib/locale/it
#%lang(ja) %{jredir}/lib/locale/ja
#%lang(ko) %{jredir}/lib/locale/ko
#%lang(ko_KR.UTF-8) %{jredir}/lib/locale/ko.UTF-8
#%lang(sv) %{jredir}/lib/locale/sv
#%lang(zh_CN) %{jredir}/lib/locale/zh
#%lang(zh_CN.GBK) %{jredir}/lib/locale/zh.GBK
#%lang(zh_TW) %{jredir}/lib/locale/zh_TW
#%lang(zh_TW) %{jredir}/lib/locale/zh_TW.BIG5

#%files -n mozilla-plugin-%{name}
#%defattr(644,root,root,755)
#%dir %{jredir}/plugin/i386/ns610
#%attr(755,root,root) %{jredir}/plugin/i386/ns610/libjavaplugin_oji.so
#%{mozilladir}/plugins/libjavaplugin_oji.so

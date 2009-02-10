# TODO:
# - better way to choose preferred jvm (currently the symlinks are hardcoded)
#   Maybe a package containing only the symlinks?
# - warning: Installed (but unpackaged) file(s) found:
#   /usr/lib/jvm/java-sun-1.6.0.10/demo/jvmti/index.html
#   /usr/lib/jvm/java-sun-1.6.0.10/jre/lib/fontconfig.RedHat.4.bfc
#   /usr/lib/jvm/java-sun-1.6.0.10/jre/lib/fontconfig.RedHat.4.properties.src
#   /usr/lib/jvm/java-sun-1.6.0.10/jre/lib/servicetag/jdk_header.png
# - dep loop (can be solved by moving shared libs to java-sun-libs):
#   java-sun-jre>java-sun-tools
#
%define		_enable_debug_packages 0
#
%define		_src_ver	6u12
%define		_dir_ver	%(echo %{version} | sed 's/\\.\\(..\\)$/_\\1/')
# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 50.0
Summary:	Sun JDK (Java Development Kit) for Linux
Summary(pl.UTF-8):	Sun JDK - środowisko programistyczne Javy dla Linuksa
Name:		java-sun
Version:	1.6.0.12
Release:	1
License:	restricted, distributable
Group:		Development/Languages/Java
Source0:	http://download.java.net/dlj/binaries/jdk-%{_src_ver}-dlj-linux-i586.bin
# Source0-md5:	560a51cfeecc4918d01ca29abc858d52
Source1:	http://download.java.net/dlj/binaries/jdk-%{_src_ver}-dlj-linux-amd64.bin
# Source1-md5:	9dce878be77b4a93337fa85b40b29069
Source2:	Test.java
Patch0:		%{name}-desktop.patch
URL:		https://jdk-distros.dev.java.net/developer.html
BuildRequires:	file
BuildRequires:	rpm-build >= 4.3-0.20040107.21
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	unzip
Requires:	%{name}-jre = %{version}-%{release}
Requires:	java-shared
Requires:	jpackage-utils >= 0:1.6.6-14
Provides:	j2sdk = %{version}
Provides:	jdk = %{version}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	java-blackdown
Obsoletes:	jdk
Obsoletes:	kaffe
Conflicts:	netscape4-plugin-java-sun
ExclusiveArch:	i586 i686 pentium3 pentium4 athlon %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		javareldir	%{name}-%{version}
%define		javadir		%{_jvmdir}/%{javareldir}
%define		jrereldir	%{javareldir}/jre
%define		jredir		%{_jvmdir}/%{jrereldir}
%define		jvmjardir	%{_jvmjardir}/%{name}-%{version}

%ifarch %{ix86}
%define		arch	i386
%endif
%ifarch %{x8664}
%define		arch	amd64
%endif


# rpm doesn't like strange version definitions provided by Sun's libs
%define		_noautoprov	'\\.\\./.*' '/export/.*'
# these with SUNWprivate.* are found as required, but not provided
# the rest is because -jdbc wants unixODBC-devel(?)
%define		_noautoreq	'libjava.so(SUNWprivate_1.1)' 'libnet.so(SUNWprivate_1.1)' 'libverify.so(SUNWprivate_1.1)' 'libodbcinst.so' 'libodbc.so' 'libjava_crw_demo_g\.so.*'
# don't depend on other JRE/JDK installed on build host
%define		_noautoreqdep	libjava.so libjvm.so

%description
Java Development Kit for Linux.

%description -l pl.UTF-8
Środowisko programistyczne Javy dla Linuksa.

%package appletviewer
Summary:	Java applet viewer from Sun Java
Summary(pl.UTF-8):	Przeglądarka appletów Javy Suna
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}

%description appletviewer
This package applet viewer for Sun Java.

%description appletviewer -l pl.UTF-8
Ten pakiet zawiera przeglądarkę appletów dla Javy Suna.

%package jre-jdbc
Summary:	JDBC files for Sun Java
Summary(pl.UTF-8):	Pliki JDBC dla Javy Suna
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
%ifarch %{x8664}
Requires:	libodbc.so.1()(64bit)
Requires:	libodbcinst.so.1()(64bit)
%else
Requires:	libodbc.so.1
Requires:	libodbcinst.so.1
%endif
Provides:	%{name}-jdbc
Obsoletes:	java-sun-jdbc

%description jre-jdbc
This package contains JDBC files for Sun Java.

%description jre-jdbc -l pl.UTF-8
Ten pakiet zawiera pliki JDBC dla Javy Suna.

%package jre
Summary:	Sun JRE (Java Runtime Environment) for Linux
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa
Group:		Development/Languages/Java
Requires:	java-jre-tools
Requires:	jpackage-utils >= 0:1.6.6-14
Requires:	rpm-whiteout >= 1.8
Provides:	j2re = %{version}
Provides:	jaas = %{version}
Provides:	jaf = 1.1.1
Provides:	java
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java1.4
Provides:	jaxp = 1.3
Provides:	jaxp_parser_impl
Provides:	jce = %{version}
Provides:	jdbc-stdext = %{version}
Provides:	jdbc-stdext = 3.0
Provides:	jmx = 1.4
Provides:	jndi = %{version}
Provides:	jndi-cos = %{version}
Provides:	jndi-dns = %{version}
Provides:	jndi-ldap = %{version}
Provides:	jndi-rmi = %{version}
Provides:	jre = %{version}
Provides:	jsse = %{version}
Provides:	xml-commons-apis
Obsoletes:	jaas
Obsoletes:	java-blackdown-jre
Obsoletes:	jaxp
Obsoletes:	jce
Obsoletes:	jdbc-stdext
Obsoletes:	jmx
Obsoletes:	jndi
Obsoletes:	jndi-provider-cosnaming
Obsoletes:	jndi-provider-dns
Obsoletes:	jndi-provider-ldap
Obsoletes:	jndi-provider-rmiregistry
Obsoletes:	jre
Obsoletes:	jsse

%description jre
Java Runtime Environment for Linux. Does not contain any X11-related
compontents.

%description jre -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa. Nie zawiera żadnych
elementów związanych ze środowiskiem X11.

%package jre-X11
Summary:	Sun JRE (Java Runtime Environment) for Linux, X11 related parts
Summary(pl.UTF-8):	Sun JRE - środowisko uruchomieniowe Javy dla Linuksa, części korzystające z X11
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	javaws = %{version}
Provides:	jre-X11 = %{version}

%description jre-X11
X11-related part of Java Runtime Environment for Linux.

%description jre-X11 -l pl.UTF-8
Środowisko uruchomieniowe Javy dla Linuksa, część związana ze
środowiskiem graficznym X11.

%package jre-alsa
Summary:	JRE module for ALSA sound support
Summary(pl.UTF-8):	Moduł JRE do obsługi dźwięku poprzez ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Provides:	%{name}-alsa
Obsoletes:	java-sun-alsa

%description jre-alsa
JRE module for ALSA sound support.

%description jre-alsa -l pl.UTF-8
Moduł JRE do obsługi dźwięku poprzez ALSA.

%package tools
Summary:	Shared Java tools
Summary(pl.UTF-8):	Współdzielone narzędzia Javy
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	rpm-whiteout >= 1.8
Provides:	jar
Provides:	java-jre-tools
Provides:	java-shared
Obsoletes:	fastjar
Obsoletes:	jar
Obsoletes:	java-jre-tools
Obsoletes:	java-shared

%description tools
This package contains tools that are common for every Java(TM)
implementation, such as rmic or jar.

%description tools -l pl.UTF-8
Pakiet ten zawiera narzędzia wspólne dla każdej implementacji
Javy(TM), takie jak rmic czy jar.

%package demos
Summary:	JDK demonstration programs
Summary(pl.UTF-8):	Programy demonstracyjne do JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Obsoletes:	java-blackdown-demos
Obsoletes:	jdk-demos

%description demos
JDK demonstration programs.

%description demos -l pl.UTF-8
Programy demonstracyjne do JDK.

%package -n browser-plugin-%{name}
Summary:	Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java-sun-mozilla-plugin
Provides:	mozilla-firefox-plugin-java-sun
Provides:	mozilla-plugin-java-sun
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java-sun-ng
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	java-sun-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java-sun
Obsoletes:	mozilla-firefox-plugin-gcc3-java-sun
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-java-sun
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java-sun
Obsoletes:	mozilla-plugin-gcc3-java-sun
Obsoletes:	mozilla-plugin-gcc32-java-sun
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun

%description -n browser-plugin-%{name}
Java plugin for WWW browsers.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka z obsługą Javy dla przeglądarek WWW.

%package -n browser-plugin-%{name}-ng
Summary:	Next-Generation Java plugin for WWW browsers
Summary(pl.UTF-8):	Wtyczka Javy Nowej Generacji do przeglądarek WWW
Group:		Development/Languages/Java
Requires:	%{name}-jre-X11 = %{version}-%{release}
Requires:	browser-plugins >= 2.0
Requires:	browser-plugins(%{_target_base_arch})
Provides:	java-sun-mozilla-plugin
Provides:	mozilla-firefox-plugin-java-sun
Provides:	mozilla-plugin-java-sun
Obsoletes:	blackdown-java-sdk-mozilla-plugin
Obsoletes:	browser-plugin-java-sun
Obsoletes:	java-blackdown-mozilla-plugin
Obsoletes:	java-sun-moz-plugin
Obsoletes:	java-sun-mozilla-plugin
Obsoletes:	jre-mozilla-plugin
Obsoletes:	mozilla-firefox-plugin-gcc2-java-sun
Obsoletes:	mozilla-firefox-plugin-gcc3-java-sun
Obsoletes:	mozilla-firefox-plugin-java-blackdown
Obsoletes:	mozilla-firefox-plugin-java-sun
Obsoletes:	mozilla-plugin-blackdown-java-sdk
Obsoletes:	mozilla-plugin-gcc2-java-sun
Obsoletes:	mozilla-plugin-gcc3-java-sun
Obsoletes:	mozilla-plugin-gcc32-java-sun
Obsoletes:	mozilla-plugin-java-blackdown
Obsoletes:	mozilla-plugin-java-sun

%description -n browser-plugin-%{name}-ng
Next-Generation Java plugin for WWW browsers. Works only with
Firefox/Iceweasel 3.x.

%description -n browser-plugin-%{name}-ng -l pl.UTF-8
Wtyczka Nowej Generacji z obsługą Javy dla przeglądarek WWW. Działa
tylko z Firefoxem/Iceweaselem 3.x.

%package sources
Summary:	JDK sources
Summary(pl.UTF-8):	Źródła JDK
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}

%description sources
Sources for package JDK.

%description sources -l pl.UTF-8
Źródła dla pakietu JDK.

%prep
%setup -q -T -c -n jdk%{_dir_ver}
cd ..
%ifarch %{ix86}
%{__unzip} -q %{SOURCE0} || :
%endif
%ifarch %{x8664}
%{__unzip} -q %{SOURCE1} || :
%endif
cd -
# patch only copy of the desktop file, leave original unchanged
cp jre/plugin/desktop/sun_java.desktop .
%patch0 -p1

# unpack packed jar files -- in %%prep as it is done "in place"
for pack in $(find . -name '*.pack'); do
	bin/unpack200 -r $pack ${pack%.pack}.jar
done

cp %{SOURCE2} Test.java

%build
# $ORIGIN does not work on PLD builders. workaround.
export LD_LIBRARY_PATH=$(pwd)/jre/lib/%{arch}/jli
./bin/javac Test.java

classver=$(file Test.class | grep -o 'compiled Java class data, version [0-9.]*' | awk '{print $NF}')
if [ "$classver" != %{_classdataversion} ]; then
	echo "Set %%define _classdataversion to $classver and rerun."
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{jredir},%{javadir},%{jvmjardir},%{_javadir},%{_bindir},%{_includedir}} \
	$RPM_BUILD_ROOT{%{_mandir}/{,ja/}man1,%{_prefix}/src/%{name}-sources} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},%{_browserpluginsdir}}

cp -a bin sample demo include lib $RPM_BUILD_ROOT%{javadir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1
install man/ja/man1/* $RPM_BUILD_ROOT%{_mandir}/ja/man1

if test -f jre/lib/i386/client/Xusage.txt; then
	mv -f jre/lib/i386/client/Xusage.txt jre/Xusage.client
fi
if test -f jre/lib/i386/server/Xusage.txt; then
	mv -f jre/lib/i386/server/Xusage.txt jre/Xusage.server
fi
if test -f jre/lib/*.txt; then
	mv -f jre/lib/*.txt jre
fi

cp -af jre/{bin,lib} $RPM_BUILD_ROOT%{jredir}

for i in java keytool orbd policytool \
	java_vm javaws \
	rmid rmiregistry servertool tnameserv pack200 unpack200; do
	[ -f $RPM_BUILD_ROOT%{jredir}/bin/$i ] || exit 1
	ln -sf %{jredir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

for i in appletviewer extcheck idlj jar jarsigner \
	javac javadoc javah javap jconsole jdb jhat jinfo jmap jps \
	jrunscript jsadebugd jstack jstat jstatd native2ascii rmic serialver \
	jvisualvm schemagen wsgen wsimport xjc apt; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

%ifarch %{ix86}
for i in HtmlConverter jcontrol java-rmi.cgi; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif
%ifarch %{x8664}
for i in HtmlConverter jcontrol; do
	[ -f $RPM_BUILD_ROOT%{javadir}/bin/$i ] || exit 1
	ln -sf %{javadir}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done
%endif

# make sure all tools are available under $(JDK_HOME)/bin
for i in keytool orbd policytool rmid \
		java_vm javaws \
		rmiregistry servertool tnameserv pack200 unpack200 java; do
	[ -f $RPM_BUILD_ROOT%{jredir}/bin/$i ] || exit 1
	ln -sf ../jre/bin/$i $RPM_BUILD_ROOT%{javadir}/bin/$i
done

# copy _all_ plugin files (even those incompatible with PLD) --
# license restriction
cp -a jre/plugin $RPM_BUILD_ROOT%{jredir}

# Install plugin for browsers
# Plugin in regular location simply does not work (is seen by browsers):
%ifarch %{ix86}
ln -sf %{jredir}/plugin/%{arch}/ns7/libjavaplugin_oji.so $RPM_BUILD_ROOT%{_browserpluginsdir}
%endif
ln -sf %{jredir}/lib/%{arch}/libnpjp2.so $RPM_BUILD_ROOT%{_browserpluginsdir}

cp -a *.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a jre/plugin/desktop/*.png $RPM_BUILD_ROOT%{_pixmapsdir}

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{jvmjardir}/jce.jar
for f in jndi jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext jdbc-stdext-3.0 \
	sasl jaxp_parser_impl jaxp_transform_impl jaxp jmx activation xml-commons-apis \
	jndi-dns jndi-rmi; do
	ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{jvmjardir}/$f.jar
done

install -d $RPM_BUILD_ROOT%{jredir}/javaws
cp -a jre/javaws/* $RPM_BUILD_ROOT%{jredir}/javaws
ln -sf %{jredir}/lib/javaws.jar $RPM_BUILD_ROOT%{jvmjardir}/javaws.jar

# leave all locale files unchanged in the original location (license
# restrictions) and only link them at the proper locations
for loc in $(ls $RPM_BUILD_ROOT%{jredir}/lib/locale); do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
	ln -sf %{jredir}/lib/locale/$loc/LC_MESSAGES/sunw_java_plugin.mo \
		$RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
done

# standardize dir names
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh,zh_CN}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{zh_HK.BIG5HK,zh_HK}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{ko.UTF-8,zh.GBK,zh_TW.BIG5}

cp -a src.zip $RPM_BUILD_ROOT%{_prefix}/src/%{name}-sources

ln -s %{javareldir} $RPM_BUILD_ROOT%{_jvmdir}/java
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/jre
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/java
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jre
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_jvmjardir}/jsse

# modify RPATH so that javac and friends are able to work when /proc is not
# mounted and we can't append to RPATH (for example to keep previous lookup
# path) as RPATH can't be longer than original
#
# for example:
# old javac: RPATH=$ORIGIN/../lib/i386/jli:$ORIGIN/../jre/lib/i386/jli
# new javac: RPATH=/usr/lib/jvm/java-sun-1.6.0/jre/lib/i386/jli

# silly rpath: jre/bin/unpack200: RPATH=$ORIGIN
chrpath -d $RPM_BUILD_ROOT%{jredir}/bin/unpack200

fixrpath() {
	execlist=$(find $RPM_BUILD_ROOT%{javadir} -type f -perm +1 | xargs file | awk -F: '/ELF.*executable/{print $1}')
	for f in $execlist; do
		rpath=$(chrpath -l $f | awk '/RPATH=/ { gsub(/.*RPATH=/,""); gsub(/:/," "); print $0 }')
		[ "$rpath" ] || continue

		# file
		file=${f#$RPM_BUILD_ROOT}
		origin=${file%/*}

		new=
		for a in $rpath; do
			t=$(echo $a | sed -e "s,\$ORIGIN,$origin,g")
			# get rid of ../../
			t=$(set -e; t=$RPM_BUILD_ROOT$t; [ -d $t ] || exit 0; cd $t; pwd)
			# skip inexistent paths
			[ "$t" ] || continue

			t=${t#$RPM_BUILD_ROOT}

			if [[ "$new" != *$t* ]]; then
				# append it now
				new=${new}${new:+:}$t
			fi
		done
		chrpath -r ${new} $f
	done
}

fixrpath

%clean
rm -rf $RPM_BUILD_ROOT

%pretrans jre
if [ -L %{jredir} ]; then
	rm -f %{jredir}
fi
if [ -L %{javadir} ]; then
	rm -f %{javadir}
fi

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%post -n browser-plugin-%{name}-ng
%update_browser_plugins

%postun -n browser-plugin-%{name}-ng
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc COPYRIGHT LICENSE README.html
%{_jvmdir}/java
%{_jvmjardir}/java
%attr(755,root,root) %{_bindir}/HtmlConverter
%ifarch %{ix86}
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%endif
%attr(755,root,root) %{_bindir}/apt
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jhat
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/schemagen
%attr(755,root,root) %{_bindir}/wsgen
%attr(755,root,root) %{_bindir}/wsimport
%attr(755,root,root) %{_bindir}/xjc
%attr(755,root,root) %{javadir}/bin/HtmlConverter
%ifarch %{ix86}
%attr(755,root,root) %{javadir}/bin/java-rmi.cgi
%endif
%attr(755,root,root) %{javadir}/bin/apt
%attr(755,root,root) %{javadir}/bin/extcheck
%attr(755,root,root) %{javadir}/bin/idlj
%attr(755,root,root) %{javadir}/bin/jarsigner
%attr(755,root,root) %{javadir}/bin/javac
%attr(755,root,root) %{javadir}/bin/javadoc
%attr(755,root,root) %{javadir}/bin/javah
%attr(755,root,root) %{javadir}/bin/javap
%attr(755,root,root) %{javadir}/bin/jconsole
%attr(755,root,root) %{javadir}/bin/jdb
%attr(755,root,root) %{javadir}/bin/jhat
%attr(755,root,root) %{javadir}/bin/jinfo
%attr(755,root,root) %{javadir}/bin/jmap
%attr(755,root,root) %{javadir}/bin/jps
%attr(755,root,root) %{javadir}/bin/jrunscript
%attr(755,root,root) %{javadir}/bin/jsadebugd
%attr(755,root,root) %{javadir}/bin/jstack
%attr(755,root,root) %{javadir}/bin/jstat
%attr(755,root,root) %{javadir}/bin/jstatd
%attr(755,root,root) %{javadir}/bin/keytool
%attr(755,root,root) %{javadir}/bin/native2ascii
%attr(755,root,root) %{javadir}/bin/orbd
%attr(755,root,root) %{javadir}/bin/rmid
%attr(755,root,root) %{javadir}/bin/rmiregistry
%attr(755,root,root) %{javadir}/bin/schemagen
%attr(755,root,root) %{javadir}/bin/serialver
%attr(755,root,root) %{javadir}/bin/servertool
%attr(755,root,root) %{javadir}/bin/tnameserv
%attr(755,root,root) %{javadir}/bin/wsgen
%attr(755,root,root) %{javadir}/bin/wsimport
%attr(755,root,root) %{javadir}/bin/xjc
%{javadir}/include
%dir %{javadir}/lib
%attr(755,root,root) %{javadir}/lib/jexec
%{javadir}/lib/ct.sym
%{javadir}/lib/*.jar
%{javadir}/lib/*.idl
%{_mandir}/man1/apt.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jconsole.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/jhat.1*
%{_mandir}/man1/jinfo.1*
%{_mandir}/man1/jmap.1*
%{_mandir}/man1/jps.1*
%{_mandir}/man1/jrunscript.1*
%{_mandir}/man1/jsadebugd.1*
%{_mandir}/man1/jstack.1*
%{_mandir}/man1/jstat.1*
%{_mandir}/man1/jstatd.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/serialver.1*
%{_mandir}/man1/schemagen.1*
%{_mandir}/man1/wsgen.1*
%{_mandir}/man1/wsimport.1*
%{_mandir}/man1/xjc.1*
%lang(ja) %{_mandir}/ja/man1/apt.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/jhat.1*
%lang(ja) %{_mandir}/ja/man1/jinfo.1*
%lang(ja) %{_mandir}/ja/man1/jmap.1*
%lang(ja) %{_mandir}/ja/man1/jps.1*
%lang(ja) %{_mandir}/ja/man1/jrunscript.1*
%lang(ja) %{_mandir}/ja/man1/jsadebugd.1*
%lang(ja) %{_mandir}/ja/man1/jstack.1*
%lang(ja) %{_mandir}/ja/man1/jstat.1*
%lang(ja) %{_mandir}/ja/man1/jstatd.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/schemagen.1*
%lang(ja) %{_mandir}/ja/man1/wsgen.1*
%lang(ja) %{_mandir}/ja/man1/wsimport.1*
%lang(ja) %{_mandir}/ja/man1/xjc.1*

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%attr(755,root,root) %{javadir}/bin/appletviewer
%{_mandir}/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*

%files jre-jdbc
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{arch}/libJdbcOdbc.so

%files jre
%defattr(644,root,root,755)
%doc jre/{COPYRIGHT,LICENSE,README,*.txt}
%doc jre/Welcome.html
%{_jvmdir}/jre
%{_jvmjardir}/jre
%{_jvmjardir}/jsse
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/unpack200
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/unpack200
%attr(755,root,root) %{javadir}/bin/pack200
%attr(755,root,root) %{javadir}/bin/unpack200
%dir %{javadir}
%dir %{javadir}/bin
%attr(755,root,root) %{javadir}/bin/java
%dir %{jredir}
%dir %{jredir}/bin
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%dir %{jredir}/lib
%{jredir}/lib/applet
%{jredir}/lib/audio
%{jredir}/lib/cmm
%{jredir}/lib/ext

%dir %{jredir}/lib/%{arch}
%dir %{jredir}/lib/%{arch}/headless
%dir %{jredir}/lib/%{arch}/jli
%attr(755,root,root) %{jredir}/lib/%{arch}/native_threads
%attr(755,root,root) %{jredir}/lib/%{arch}/server
%attr(755,root,root) %{jredir}/lib/%{arch}/jli/libjli.so
%{jredir}/lib/%{arch}/jvm.cfg
%attr(755,root,root) %{jredir}/lib/%{arch}/lib[acdfhijmnrvz]*.so
%exclude %{jredir}/lib/%{arch}/libjsoundalsa.so
%ifarch %{ix86}
%attr(755,root,root) %{jredir}/lib/%{arch}/client
%endif
%attr(755,root,root) %{jredir}/lib/%{arch}/libsplashscreen.so
%exclude %{jredir}/lib/%{arch}/libjavaplugin*.so

%{jredir}/lib/deploy
%{jredir}/lib/desktop
%{jredir}/lib/im
%{jredir}/lib/images
%attr(755,root,root) %{jredir}/lib/jexec
%{jredir}/lib/meta-index
%dir %{jredir}/lib/security
%{jredir}/lib/security/*.*
%verify(not md5 mtime size) %config(noreplace) %{jredir}/lib/security/cacerts
%{jredir}/lib/zi
%{jredir}/lib/*.jar
%{jredir}/lib/*.properties
%lang(ja) %{jredir}/lib/*.properties.ja
%dir %{jvmjardir}
%{jvmjardir}/activation.jar
%{jvmjardir}/jaas.jar
%{jvmjardir}/jce.jar
%{jvmjardir}/jcert.jar
%{jvmjardir}/jdbc-stdext*.jar
%{jvmjardir}/jmx.jar
%{jvmjardir}/jndi*.jar
%{jvmjardir}/jnet.jar
%{jvmjardir}/jsse.jar
%{jvmjardir}/sasl.jar
%{jvmjardir}/jaxp*.jar
%{jvmjardir}/xml-commons*.jar
%{jredir}/lib/classlist
%{jredir}/lib/fontconfig.RedHat.2.1.bfc
%{jredir}/lib/fontconfig.RedHat.2.1.properties.src
%{jredir}/lib/fontconfig.RedHat.3.bfc
%{jredir}/lib/fontconfig.RedHat.3.properties.src
%{jredir}/lib/fontconfig.RedHat.bfc
%{jredir}/lib/fontconfig.RedHat.properties.src
%{jredir}/lib/fontconfig.SuSE.bfc
%{jredir}/lib/fontconfig.SuSE.properties.src
%{jredir}/lib/fontconfig.Sun.bfc
%{jredir}/lib/fontconfig.Sun.properties.src
%{jredir}/lib/fontconfig.Turbo.bfc
%{jredir}/lib/fontconfig.Turbo.properties.src
%{jredir}/lib/fontconfig.bfc
%{jredir}/lib/fontconfig.properties.src
%attr(755,root,root) %{jredir}/lib/%{arch}/headless/libmawt.so
%attr(755,root,root) %{jredir}/lib/%{arch}/libsaproc.so
%attr(755,root,root) %{jredir}/lib/%{arch}/libunpack.so
%dir %{jredir}/lib/management
%{jredir}/lib/management/jmxremote.access
%{jredir}/lib/management/jmxremote.password.template
%{jredir}/lib/management/management.properties
%{jredir}/lib/management/snmp.acl.template
%{_mandir}/man1/java.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%{_mandir}/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/*pack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*

%files jre-X11
%defattr(644,root,root,755)
%ifarch %{ix86}
%doc jre/Xusage*
%endif
%attr(755,root,root) %{_bindir}/java_vm
%attr(755,root,root) %{_bindir}/javaws
%attr(755,root,root) %{_bindir}/jcontrol
%attr(755,root,root) %{jredir}/bin/ControlPanel
%attr(755,root,root) %{jredir}/bin/java_vm
%attr(755,root,root) %{jredir}/bin/javaws
%attr(755,root,root) %{jredir}/bin/jcontrol
%attr(755,root,root) %{javadir}/bin/ControlPanel
%attr(755,root,root) %{javadir}/bin/java_vm
%attr(755,root,root) %{javadir}/bin/javaws
%attr(755,root,root) %{javadir}/bin/jcontrol
%{_desktopdir}/sun_java.desktop
%{_pixmapsdir}/sun_java.png
%attr(755,root,root) %{_bindir}/jvisualvm
%attr(755,root,root) %{_bindir}/policytool
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{javadir}/bin/policytool
%{_mandir}/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*
%attr(755,root,root) %{javadir}/bin/jvisualvm
%{_mandir}/man1/jvisualvm.1*
%lang(ja) %{_mandir}/ja/man1/jvisualvm.1*
%{javadir}/lib/visualvm
%{jredir}/lib/fonts
%{jredir}/lib/oblique-fonts
%dir %{jredir}/lib/%{arch}/xawt
%dir %{jredir}/lib/%{arch}/motif21
%attr(755,root,root) %{jredir}/lib/%{arch}/libsplashscreen.so
%{jvmjardir}/javaws.jar
%attr(755,root,root) %{jredir}/lib/%{arch}/motif21/libmawt.so
%attr(755,root,root) %{jredir}/lib/%{arch}/xawt/libmawt.so
%dir %{jredir}/lib/locale
%lang(de) %{jredir}/lib/locale/de
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/sunw_java_plugin.mo
%lang(es) %{jredir}/lib/locale/es
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/sunw_java_plugin.mo
%lang(fr) %{jredir}/lib/locale/fr
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/sunw_java_plugin.mo
%lang(it) %{jredir}/lib/locale/it
%lang(it) %{_datadir}/locale/it/LC_MESSAGES/sunw_java_plugin.mo
%lang(ja) %{jredir}/lib/locale/ja
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/sunw_java_plugin.mo
%lang(ko) %{jredir}/lib/locale/ko*
%lang(ko) %{_datadir}/locale/ko/LC_MESSAGES/sunw_java_plugin.mo
%lang(sv) %{jredir}/lib/locale/sv
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_CN) %{jredir}/lib/locale/zh
%lang(zh_CN) %{jredir}/lib/locale/zh.*
%lang(zh_HK) %{jredir}/lib/locale/zh_HK*
%lang(zh_HK) %{_datadir}/locale/zh_HK/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{jredir}/lib/locale/zh_TW*
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/sunw_java_plugin.mo
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/sunw_java_plugin.mo
%dir %{jredir}/javaws
%attr(755,root,root) %{jredir}/javaws/javaws
%{_mandir}/man1/javaws.1*
%ifarch %{ix86}
%lang(ja) %{_mandir}/ja/man1/javaws.1*
%endif

%files jre-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{arch}/libjsoundalsa.so

%files demos
%defattr(644,root,root,755)
%dir %{javadir}/demo
%{javadir}/demo/applets
%{javadir}/demo/jfc
%{javadir}/demo/jpda
%dir %{javadir}/demo/jvmti
%dir %{javadir}/demo/jvmti/[!i]*
%dir %{javadir}/demo/jvmti/*/lib
%attr(755,root,root) %{javadir}/demo/jvmti/*/lib/*.so
%{javadir}/demo/jvmti/*/src
%{javadir}/demo/jvmti/*/README*
%{javadir}/demo/jvmti/*/*.jar
%{javadir}/demo/management
%{javadir}/demo/nbproject
%{javadir}/demo/plugin
%{javadir}/demo/applets.html
%{javadir}/demo/scripting
%{javadir}/sample

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

%ifarch %{ix86}
%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%dir %{jredir}/plugin
%dir %{jredir}/plugin/%{arch}
%dir %{jredir}/plugin/%{arch}/ns7
%dir %{jredir}/plugin/%{arch}/ns7-gcc29
# XXX: duplicate
%attr(755,root,root) %{jredir}/lib/%{arch}/libjavaplugin*.so
%attr(755,root,root) %{jredir}/plugin/%{arch}/*/libjavaplugin_oji.so
%attr(755,root,root) %{_browserpluginsdir}/libjavaplugin_oji.so
%{jredir}/plugin/desktop
%endif

%files -n browser-plugin-%{name}-ng
%defattr(644,root,root,755)
%dir %{jredir}/plugin
# XXX: duplicate
%attr(755,root,root) %{jredir}/lib/%{arch}/libjavaplugin*.so
%attr(755,root,root) %{jredir}/lib/%{arch}/libnpjp2.so
%attr(755,root,root) %{_browserpluginsdir}/libnpjp2.so
%{jredir}/plugin/desktop

%files sources
%defattr(644,root,root,755)
%dir %{_prefix}/src/%{name}-sources
%{_prefix}/src/%{name}-sources/src.zip

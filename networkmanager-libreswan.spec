%define nmversion	%(echo %{version} | cut -d "." -f -2)
%define url_ver		%(echo %{version}|cut -d. -f1,2)

%define _disable_ld_no_undefined 1

# filter out plugin .so provides
%global __provides_exclude_from %{_libdir}/NetworkManager/.*\\.so

Summary:	NetworkManager VPN integration for LibreSWAN
Name:		networkmanager-libreswan
Version:	1.2.16
Release:	1
License:	GPLv2+
Group:		System/Base
URL:		https://wiki.gnome.org/Projects/NetworkManager
Source0:	https://download.gnome.org/sources/NetworkManager-libreswan/%{url_ver}/NetworkManager-libreswan-%{version}.tar.xz
BuildRequires:	gettext
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(libnma) >= %{nmversion}
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libsecret-unstable)
Requires:	NetworkManager
Requires:	shared-mime-info
Obsoletes:	networkmanager-openswan <= 1.1.0

%description
This package contains software for integrating the LibreSWAN IPSec VPN software
with NetworkManager.

%prep
%setup -qn NetworkManager-libreswan-%{version}
%autopatch -p1

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure \
	--disable-static \
	--without-libnm-glib \
	--with-gtk4
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang NetworkManager-libreswan

%files -f NetworkManager-libreswan.lang
%doc AUTHORS ChangeLog README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/nm-libreswan-service.conf
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-libreswan-editor.so
%{_libexecdir}/nm-libreswan-auth-dialog
%{_libexecdir}/nm-libreswan-service
%{_libexecdir}/nm-libreswan-service-helper
#dir %{_datadir}/gnome-vpn-properties/libreswan
#{_datadir}/gnome-vpn-properties/libreswan/nm-libreswan-dialog.ui
#{_datadir}/appdata/network-manager-libreswan.metainfo.xml
%{_usr}/lib/NetworkManager/VPN/nm-libreswan-service.name
%{_mandir}/man5/nm-settings-libreswan.5.*

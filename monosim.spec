%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Manage your SIM Card contacts
Name:		monosim
Version:	1.5.2
Release:	5
License:	GPLv2+
Group:		Office
Url:		http://www.integrazioneweb.com/monosim
Source0:	http://www.integrazioneweb.com/repository/sources/%{name}-%{version}.tar.gz
Patch0:		monosim-1.5.2-fix-desktop-file.patch
BuildRequires:	glade-sharp2 >= 2.8.3
BuildRequires:	mono >= 1.2.3
Requires:	gtk-sharp2 >= 2.8.3
Requires:	mono >= 1.2.3
Requires:	pcsc-lite >= 1.0.0
# libpcsclite-devel required because contain /usr/lib/libpcsclite.so
# not contained in to libpcsclite1
Requires:	pkgconfig(libpcsclite)

%description
is a simple application that can be used to read, write, update,
delete and backup your sim card contacts. It open and save also
some format files to manage your contacts also in a text files.
To connect monosim to your smartcard you need use a standard PCSC
smartcard reader as towitoko, acs, athena, blutronics, etc.

%files
%doc monosim/copying.gpl
%{_libdir}/%{name}/
%{_bindir}/monosim
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std


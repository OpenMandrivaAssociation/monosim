Summary: Manage your SIM Card contacts
Name: monosim
Version: 1.5.2
Release: %mkrel 1
License: GPLv2
Group: Office
Source: http://www.integrazioneweb.com/repository/sources/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://www.integrazioneweb.com/monosim

#BuildRequires: gtk-sharp2-devel >= 2.8.3
BuildRequires: glade-sharp2 >= 2.8.3
BuildRequires: mono >= 1.2.3
BuildRequires: pkgconfig

Requires: gtk-sharp2 >= 2.8.3
Requires: mono >= 1.2.3
Requires: pcsc-lite >= 1.0.0
Requires: libpcsclite1 >= 1.0.0
# libpcsclite-devel required because contain /usr/lib/libpcsclite.so
# not contained in to libpcsclite1
Requires: libpcsclite-devel >= 1.0.0


%description
is a simple application that can be used to read, write, update,
delete and backup your sim card contacts. It open and save also
some format files to manage your contacts also in a text files.
To connect monosim to your smartcard you need use a standard PCSC
smartcard reader as towitoko, acs, athena, blutronics, etc.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %{buildroot}
# %makeinstall_std linuxpkgconfigdir=%{_datadir}/pkgconfig
%makeinstall_std


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc monosim/copying.gpl
%{_libdir}/%{name}/
%{_bindir}/monosim
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Jul 18 2009 A.Basile <hmandevteam@gmail.com> 1.5.2-1mdv2010.0
- bug fixed: issue 4/5 - fix verified (pin1 enable/disable)
- bug fixed: issue 6 - fix verified (monosim on 64 bit)
- bug fixed: issue 7 - fix verified (international numbers)
- bug fixed: issue 8  - fix verified (closing main window)
- bug fixed: cross compile compatibility (monodevelop, #develop)
- deleted pkgconfig file for monopcsclib
- modified monosim.desktop file (compliant to desktop-file-validate)


* Mon Apr 20 2009 A.Basile <hmandevteam@gmail.com> 1.4.0.1-1mdv2010.0
- issue n.4 - add PIN1 enable/disable feature
- settings filename changed in "~/.monosim"
- settings file type changed in standard xml
- no more require system.web

* Mon Jul 02 2007 hman <hmandevteam@gmail.com> 1.3.0.1-4mdv2009.0
- bug fixed: Fixed wrong label position reference in language files
- added support informations in language files
- added xml settings file to store selected language

* Sat Jun 30 2007 hman <hmandevteam@gmail.com> 1.2.0-1
- bug fixed: Many bugs fixed
- multilanguage support added (with text files in [languages] subfolder)
- erase sim phonebook function added

* Mon Jun 11 2007 hman <hmandevteam@gmail.com> 1.0.1-1
- first public release


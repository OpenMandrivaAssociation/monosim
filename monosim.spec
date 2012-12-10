Summary: Manage your SIM Card contacts
Name: monosim
Version: 1.5.2
Release: %mkrel 3
License: GPLv2
Group: Office
Source: http://www.integrazioneweb.com/repository/sources/%{name}-%{version}.tar.gz
Patch0: monosim-1.5.2-fix-desktop-file.patch
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
%patch0 -p0

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
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-3mdv2011.0
+ Revision: 612927
- the mass rebuild of 2010.1 packages

* Sat May 01 2010 Funda Wang <fwang@mandriva.org> 1.5.2-2mdv2010.1
+ Revision: 541455
- fix desktop file

* Sat Jul 18 2009 Armando Basile <hman@mandriva.org> 1.5.2-1mdv2010.0
+ Revision: 397204
- bug fix release

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.3.0.1-4mdv2009.0
+ Revision: 268148
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 04 2008 hman-it <hman-it> 1.3.0.1-3mdv2009.0
+ Revision: 214900
- spec file changed
- import monosim


* Thu May 06 2008 Armando Basile <hman@mandriva.org> 1.3.0.1-2mdv2009.0
- bug fixed: Fixed wrong label position reference in language files
- added support informations in language files
- added xml settings file to store selected language

* Sat Jun 30 2007 hman <hmandevteam@gmail.com> 1.2.0-1
- bug fixed: Many bugs fixed
- multilanguage support added (with text files in [languages] subfolder)
- erase sim phonebook function added

* Mon Jun 11 2007 hman <hmandevteam@gmail.com> 1.0.1-1
- first public release


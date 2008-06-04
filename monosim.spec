Summary:        Manage your sim card contacts with pcsc reader
Name:           monosim
Version:        1.3.0.1
Release:        %mkrel 3
License:        GPLv2
Group:          Office
Source:         http://www.integrazioneweb.com/monosim/packages/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
URL:            http://www.integrazioneweb.com/monosim

BuildArch:      noarch

BuildRequires:  gtk-sharp2-devel >= 2.8.3
BuildRequires:  glib-sharp2 >= 2.8.3
BuildRequires:  glade-sharp2 >= 2.8.3
BuildRequires:  mono-web >= 1.2.3
BuildRequires:  mono >= 1.2.3
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig

Requires:       gtk-sharp2 >= 2.8.3
Requires:       glib-sharp2 >= 2.8.3
Requires:       mono >= 1.2.3
Requires:       mono-web >= 1.2.3
Requires:       pcsc-lite
Requires:       libpcsclite1
# devel package is required because contains /usr/lib/libpcsclite.so
# that is used by monosim
Requires:       libpcsclite-devel


%description
Is a simple application that can be used to read, write, update,
delete and backup your sim card contacts. It open and save also
some format files to manage your contacts also in a text files.
To connect monosim to your smartcard you need use a standard PCSC
smartcard reader as towitoko, acs, athena, blutronics, etc.

%prep
%setup -q

%build
%configure2_5x --libdir=%_prefix/lib
%make

%install
rm -fr %{buildroot}
%makeinstall_std linuxpkgconfigdir=%{_datadir}/pkgconfig
desktop-file-install --vendor="mandriva"               \
  --dir=%{buildroot}%{_datadir}/applications    \
  monoSIM/images/%{name}.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc copying.gpl
%{_bindir}/%{name}
%_prefix/lib/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mandriva-monosim.desktop
%{_datadir}/pkgconfig/
